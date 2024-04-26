from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.shortcuts import render, get_object_or_404, redirect
from .models import taskshow
from .forms import TaskForm
from django.http import JsonResponse,HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .models import registerdetails,Feedback
from django.http import JsonResponse
from .models import Task
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
def get_tasks(request):
    date = request.GET.get('date')
    matching_tasks = taskshow.objects.filter(deadline=date).order_by('deadline')
    tasks_data = [
        {
            'name': task.name,
            'description': task.description,
            'deadline': task.deadline.strftime('%Y-%m-%d'),
            'subject': task.subject
        }
        for task in matching_tasks
    ]
    return JsonResponse(tasks_data, safe=False)

def main(request):
    return render(request, "index.html")

def vtask(request):
    t = taskshow.objects.all()
    return render(request, "vtask.html", {'t': t})

def task(request):
    if request.method == "POST":
        name = request.POST.get('task_name')
        description = request.POST.get('description')
        deadline=request.POST.get('deadline')
        subject=request.POST.get('subject')
        t = taskshow.objects.create(name=name, description=description,deadline=deadline,subject=subject)
        subject = 'New Task Created'
        message = f'A new task "{name}" has been created.\nDescription: {description}\nDeadline: {deadline}\nSubject: {subject}'
        try:
            send_mail(subject, message, settings.EMAIL_HOST_USER, [settings.EMAIL_RECIPIENT])
            messages.success(request, 'Email notification sent successfully!')
        except Exception as e:
            messages.error(request, f'Failed to send email notification: {e}')
        return redirect('vtask.html')
    return render(request, "task.html")

def updtask(request, pk):
    task = get_object_or_404(taskshow, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('vtask')
        else:
            print(form.errors)
            return render(request, 'updtask.html', {'form': form, 'task': task})
    else:
        form = TaskForm(instance=task)
    return render(request, 'updtask.html', {'form': form})

def deltask(request, pk):
    task = get_object_or_404(taskshow, pk=pk)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted successfully.')  # Success message
        return redirect('vtask')  # Redirect after deletion
    return redirect('vtask')  # Redirect if not a POST request
def home(request):
    return render(request, "dashboard.html")


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if user with this email already exists
        if registerdetails.objects.filter(username=username).exists():
            messages.error(request, 'username already exists.')
            return render(request, "register.html")

        # If email is unique, create the user
        else:
            user = registerdetails.objects.create_user(name=username, email=email, password=password)
            user.save()
            messages.info(request,'Account Created Successfully')
            return redirect('main')

    return render(request, "register.html")

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')  # Update to match the form field names
        password = request.POST.get('password')

        # Authenticate user using email and password
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard upon successful login
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('dashboard')

    return render(request, "login.html")


def sdetails(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = registerdetails.objects.create(name=name, email=email, password=password)
        user.save()
    return render(request,"login.html")


def calendar(request):
    return render(request,"calendar.html")

def aboutus(request):
    return render(request, "aboutus.html")

def contactus(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        textarea= request.POST.get('textarea')
        contact = Feedback.objects.create(name=name, email=email, textarea=textarea)
        contact.save()
    return render(request, "contactus.html")

def calendar_view(request):
    return render(request, "calendar.html")
