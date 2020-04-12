from django.conf.urls import url
from . import views
from django.urls import path, re_path
from django.contrib.auth import views as auth_views

app_name = 'team1webapp'

urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
	path('authenticate', views.viewAuth, name='authenticate'),

	
	path('class/<int:pk>/delete/', views.class_delete, name='class_delete'),
	path('class/<int:pk>/edit/', views.class_edit, name='class_edit'),  #Edit is currently out of scope for this Sprint
	path('class/create/', views.class_new_function, name='class_new'),
	
	
	path('class/<int:pk>/assignment/create/', views.assignment_new_function, name='assignment_new'),
	path('class/assignment/delete/<int:pk>/', views.assignment_delete, name='assignment_delete'),


	path('course_summary/', views.course_summary, name='course_summary'),
	path('course_summary/<int:pk>/course_summary_assignment', views.course_summary_asisgnments, name='assignment_summary'),
	path('course_summary/<int:pk>/course_summary_calculate_grade', views.course_summary_calculate_grade, name='update_grade'),

	path('create_assignment_reminder/<int:assignmentPK><int:classPK>', views.create_assignment_reminder, name='create__assignment_reminder'),
	path('<int:pk><str:time_delay>', views.create_reminder, name='create_reminder'),

	path('accounts/register', views.register, name='register'),
	path('accounts/login', views.login, name='login'),
	path('accounts/resetpassword', views.resetpassword, name='resetpassword'),
	path('accounts/logout', views.logout, name='logout'),



	#path('password_reset', views.resetpassword, name='password_reset'),
	# Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
	path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), name='password_change'),
	path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
	path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
]