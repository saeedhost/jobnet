from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from UserAccounts.forms import DataForm, CommentForm
from UserAccounts.models import PostJobData, UserComment, UserProfile
import datetime
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail



def user_register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname2')
        lname = request.POST.get('lname2')
        username = request.POST.get('username2')
        password1 = request.POST.get('pass2')
        password2 = request.POST.get('cpass2')
        if password1 != password2:
            messages.error(request, "Passwords Do not Match")
            return redirect('userReg')
        
        if len(username) < 3:
            messages.error(request, "Username must be at least 3 characters")
            return redirect('userReg')
        
        if len(username) > 16:
            messages.error(request, "Username must be less than 16 characters")
            return redirect('userReg')
        
        else:
            try:
                user = User.objects.create_user(username, None, password1)
                user.first_name=fname
                user.last_name=lname
                user.save()
                messages.success(request, "Account created successfully")
                return redirect('myHome')
            except:
                messages.error(request, "Username already exist")
                return redirect('userReg')
    else:
        form = UserCreationForm()
        return render(request, 'registration.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('myHome')
        else:
            messages.error(request, "Invalid login credentials.")
            return redirect('userLogin')
    else:
        return render(request, 'login.html')
    
@login_required(login_url="/")
def user_logout(request):
    logout(request)
    return redirect('userLogin')

@login_required(login_url="/")
def home(request):
    all_jobs = PostJobData.objects.all()
    if request.method=="POST":
        search=request.POST.get('job_search')
        if search!=None:
            all_jobs = PostJobData.objects.filter(job_location__icontains=search)

    data = {
        'jobs':all_jobs,
    }
    return render(request, "home.html", data)

@login_required(login_url="/")
def about(request):
    return render(request, "about.html")

@login_required(login_url="/")
def contact(request):
    if request.method=="POST":
        subject=request.POST.get('subject')
        user_email=request.POST.get('user_email')
        message=request.POST.get('message')

        if subject and user_email and message != '':
            send_mail(
                subject,
                message,
                user_email,
                ['saeedwtech@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, 'Email sent Successfully!')
            return redirect('contactus')
        else:
            messages.error(request, 'Email not send')
            return redirect('contactus')
    return render(request, "contact.html")

@login_required(login_url="/")
def job_details(request, job_title_ref):
    current_job_details= PostJobData.objects.get(slud_ref=job_title_ref)
    comments_count = UserComment.objects.all().count()

    slugdata={
        'current_job': current_job_details,
        'comments_count':comments_count
    }
    return render(request, "jobs-details.html", slugdata)

@login_required(login_url="/")
def upload_jobs(request):
    if request.method == 'POST':
        form = DataForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('myHome')
    else:
        form = DataForm()
    return render(request, "upload-job.html", {'form': form})

@login_required(login_url="/")
def add_comment_to_job(request, pk):
    job = PostJobData.objects.get(id=pk)
    form = CommentForm(instance=job)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=job)
        if form.is_valid():
            user_name = request.user.username
            user = User.objects.get(username=user_name)
            comment_text = form.cleaned_data['text']
            c = UserComment(commenter=user, job=job, text=comment_text, commented_at=datetime.datetime.now())
            c.save()
            return redirect('myHome')

        else:
            print("Invalid form data")
    else:
        form = CommentForm()

    data = {
        'form':form
        }

    return render(request, 'add_comment.html', data )

@login_required(login_url="/")
def user_profile(request):
    cur_user = UserProfile.objects.get(user=request.user)
    return render(request, 'header.html', {'current_user':cur_user} )

