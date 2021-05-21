from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.models import User
from videos.models import UserProfile
from django.conf import settings


def Home(request):
    if request.user.is_authenticated:
        return render(request,'./home.html', {'username': request.user.username})
        
    else:
        return redirect('../login')

def Index(request):
    return render(request,'./index.html')

def LoginView(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect( 'home')
        
        else: 
            return render(request, './login.html',{'error':'username or password is incorrect.'})
    else:
        return render(request, './login.html')


@login_required
def LogoutView(request):
    auth.logout(request)
    return redirect('../login')

def SignupView(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'error':'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'],  password=request.POST['password1'],email=request.POST['email'],
                                            first_name=request.POST['firstname'],
                                            last_name=request.POST['lastname'])
                #also create a UserProfile
                userprofile = UserProfile()
                userprofile.user = user
                userprofile.first_name = user.first_name

                userprofile.username = user.username
                userprofile.email = user.email

                form = (request.POST, request.FILES)
                if request.FILES.get('picture'):
                    userprofile.picture = request.FILES('picture')
                else:
                    userprofile.picture = settings.MEDIA_ROOT+'\images\defaultprofilepicture.png'
               
                userprofile.contact_no = request.POST.get('contact_no')

                userprofile.save()


                auth.login(request,user)
                return redirect('home')
        else:
            return render(request, './signup.html', {'error':'Passwords must match'})
    else:
        # User wants to enter info
        return render(request, './signup.html')
