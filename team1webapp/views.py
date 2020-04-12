from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .tasks import *
import datetime



def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['username']
        _email = request.POST['email']
        _password = request.POST['password']
        _password_confirm = request.POST['password_confirm']
        
        if _password == _password_confirm:
            if not User.objects.filter(username = user_name).exists():
                if not User.objects.filter(email = _email).exists():
                    user = User.objects.create_user(
                            first_name = first_name, 
                            last_name = last_name, 
                            username = user_name,
                            password = _password,
                            email = _email
                        )
                    user.save()
                    print("User Created")
                    return redirect('/')
                else:
                    messages.info(request, "Email Taken")
                    return redirect('/authenticate')
            else:
                messages.info(request, "Username Taken")
                return redirect('/authenticate')
        else:
            messages.info(request, "Password does not match")
            return redirect('/authenticate')
        
    else:
        return HttpResponse("Something Went Wrong")

def login(request):
    if request.method == "POST":
        _username = request.POST['username']
        _password = request.POST['login_password']

        user = auth.authenticate(username = _username, password = _password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Incorrect Credentials.")
            return redirect('/authenticate')
    else:
        return redirect('/authenticate')

@login_required
def logout(request):
    auth.logout(request)
    return redirect('/authenticate')

def resetpassword(request):
    return render(request, 'password_reset.html')



@login_required
def home(request):
    classes = Class.objects.filter(author_id=request.user)
    print(classes)
    return render(request, 'team1webapp/home.html', {'courses': classes})

def viewAuth(request):
    return render(request, 'accounts.html')



@login_required
def class_delete(request, pk):
    try:
        assignments = get_object_or_404(Assignment, class_name_id=pk, author_id=request.user)
        assignments.delete()
    except:
        print("NO Assignment")
    classes = get_object_or_404(Class, pk=pk, author_id=request.user)
    classes.delete()
    return redirect('/')


@login_required
def class_edit(request, pk):
    customer = get_object_or_404(Class, pk=pk)
    if request.method == "POST":
        # update
        form = ClassForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.updated_date = timezone.now()
            customer.save()
            return redirect('/')
    else:
        # edit
        return render(request, 'class_edit.html', {'id': pk})

@login_required
def class_new_function(request):
    if request.method == "POST":
        class_name = request.POST['class_name']
        point_goal = request.POST['point_goal']
        actual_points = request.POST['actual_points']
        total_points = request.POST['total_points']

        clas = Class(
            author_id = request.user.id,
            class_name = class_name,
            point_goal = point_goal,
            actual_points = actual_points,
            total_points = total_points,
                    )
        clas.save()
        print("Class Created")
        return redirect('/')
    else:
        form = ClassForm()
        return render(request, 'class_new.html', {'form': form})



@login_required
def course_summary(request):
    classes = Class.objects.filter(author_id=request.user)
    return render(request, 'team1webapp/course_summary.html', {'classes': classes})

@login_required()
def course_summary_asisgnments(request, pk):
    the_class = get_object_or_404(Class, pk=pk)
    class_name=the_class.class_name
    assignments = Assignment.objects.filter(class_name__class_name__contains=class_name, author_id = the_class.author_id)
    return render(request, 'team1webapp/course_summary_assignment.html', {'assignments': assignments, 'the_class': the_class})

@login_required()
def course_summary_calculate_grade(request, pk):
    the_class = get_object_or_404(Class, pk=pk)
    total_points = 0
    real_points = 0
    class_name = the_class.class_name
    assignments = Assignment.objects.filter(class_name__class_name__contains=class_name, author_id=the_class.author_id)
    for assignment in assignments:
        total_points = total_points + assignment.max_points
        real_points = real_points + assignment.earned_points
    the_class.total_points = total_points
    the_class.actual_points = real_points
    the_class.save()
    return redirect('team1webapp:assignment_summary', pk=pk)

@login_required
def create_assignment_reminder(request, assignmentPK, classPK):
    the_class = get_object_or_404(Class, pk=classPK)
    the_assignment = get_object_or_404(Assignment, pk=assignmentPK)

    return render(request, 'team1webapp/create_assignment_reminder.html', {'the_assignment': the_assignment, 'the_class': the_class})

@login_required
def create_reminder(request, pk , time_delay):
    the_assignment = get_object_or_404(Assignment, pk=pk)
    if time_delay == "1":
        send_time = the_assignment.due_date - datetime.timedelta(hours=1)
    elif time_delay == "2":
        send_time = the_assignment.due_date - datetime.timedelta(days=1)
    else:
        send_time = the_assignment.due_date - datetime.timedelta(weeks=1)
    print(send_time)
    send_email_reminder.apply_async((request.user.email, the_assignment.due_date.date(), the_assignment.assignment_name), eta=send_time)

    return redirect('team1webapp:course_summary')

#Add assignment to the
@login_required
def assignment_new_function(request, pk):
    if request.method == "POST":
        assignment_name = request.POST['assignment_name']
        max_points = request.POST['max_points']
        earned_points = request.POST['earned_points']
        due_date = request.POST['due_date']

        assignment = Assignment(
            author_id = request.user.id,
            assignment_name = assignment_name,
            max_points = max_points,
            earned_points = earned_points,
            due_date = due_date,
            class_name_id = pk,
                    )
        assignment.save()
        print("Assignment Created")
        return redirect('/course_summary/'+ str(pk) +'/course_summary_assignment')
    else:
        form = AssignmentForm()
        return render(request, 'assignment_new.html', {'form': form, 'class_id': pk})
    
    customer = get_object_or_404(Class, pk=pk)
    if request.method == "POST":
        # update
        form = ClassForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.updated_date = timezone.now()
            customer.save()
            return redirect('/')
    else:
        # edit
        return render(request, 'assignment_new.html', {'id': pk})

#Delete assignment to the
@login_required
def assignment_delete(request, pk):
    assignments = get_object_or_404(Assignment, pk=pk, author_id=request.user)
    assignments.delete()
    return redirect('/')