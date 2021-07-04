from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from blog.models import Post

# Create your views here.

def home(request):
    allPosts = Post.objects.all()
    context = {'allPosts':allPosts}
    return render(request, 'home/home.html', context)
def charitr(request):
    return render(request, 'home/charitr.html')
def wada(request):
    return render(request, 'home/wada.html')
def rajguru(request):
    return render(request, 'home/rajguru.html')
def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername,password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, 'logged in successfully')
            return redirect('/')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('/')
    else:
        return HttpResponse('404 Not Found')
        
def handleLogout(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'logged out successfully')
        return redirect('/')
    else:
        return HttpResponse('404 Not Found')
        
def handleSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']

        if len(username) >= 20:
            messages.warning(request, 'Username must be under 20 character')
            return redirect('home')
        if not username.isalnum():
            messages.warning(request, 'Username should only contains letters and numbers')
            return redirect('home')
        if len(password) <= 3:
            messages.warning(request, 'Password must be above 20 character')
            return redirect('home')

        # creating user
        user = User.objects.create_user(username,email,password)
        user.first_name = fname
        user.last_name = lname
        user.save()
        messages.success(request, 'Sign up in successfully')
        return redirect('home')
    else:
        return HttpResponse('404 Not Found')