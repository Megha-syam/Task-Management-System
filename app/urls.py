from django.urls import path,include
from . import views
from . views import *

urlpatterns=[
    path('',main,name="main"),
    path('login', login, name="login"),
    path('register', register, name="register"),
    path('contactus',contactus,name="contactus"),
    path('aboutus',aboutus,name="aboutus"),
    path('dashboard.html',home,name="dashboard" ),

    path('calendar.html',calendar,name="calendar"),

    path('task.html',task,name="task"),
    path('vtask.html',vtask,name="vtask"),

    path('sdetails',sdetails,name="sdetails"),

    path('get_tasks', get_tasks, name='get_tasks'),
    path('updtask/<int:pk>/', views.updtask, name="updtask"),
    path('deltask/<int:pk>/', views.deltask, name='deltask'),

    path('calendar', calendar_view, name='calendar'),

]