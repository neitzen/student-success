from django.core.mail import send_mail
from celery import shared_task

@shared_task
def send_email_reminder(usr, due_date, assignment_name):
    send_mail('You have an Upcoming Assignment',
              assignment_name + ' is due ' + due_date,
              'successstudent6@gmail.com',
              [usr])
    return None