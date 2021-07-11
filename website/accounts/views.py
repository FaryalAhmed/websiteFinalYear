from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.models import User
from videos.models import UserProfile
from django.contrib import messages 
from django.conf import settings
from .helpers import send_forget_password_mail

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
            return redirect('home')
        
        else: 
            return render(request, './login.html', messages.add_message(request, messages.ERROR, 'Incorrect Username or Password'))
    else:
        return render(request, './login.html')

@login_required
def LogoutView(request):
    auth.logout(request)
    return redirect('../login')

def SignupView(request):
    if request.user.is_authenticated:    
        return redirect('../login')

    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try: 
                if User.objects.filter(username = request.POST['username']).first():
                    return render(request, 'signup.html',messages.add_message(request, messages.ERROR, 'Username has already been taken'))
                if User.objects.filter(email = request.POST['email'].lower()).first():
                    return render(request, 'signup.html',messages.add_message(request, messages.ERROR, 'Email has already been taken'))
                
                user = User.objects.create_user(username=request.POST['username'],  password=request.POST['password1'],email=request.POST['email'].lower(),
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

                # auth.login(request,user)
                return redirect('../login',messages.add_message(request, messages.SUCCESS, 'Account Created Successfully, Login to Continue'))
            except Exception as e:
                print(e)
                return render(request , 'signup.html')
        else:
            return render(request, './signup.html',messages.add_message(request, messages.ERROR, "Passwords didn't matched") )
    else: 
        # User wants to enter info
        return render(request, './signup.html')

def Contact(request):
    if request.user.is_authenticated:
        return render(request,'./contactUs.html', {'username': request.user.username})
        
    else:
        return redirect('../login')
def ChangePassword(request , token):
    context = {}
    try:
        profile_obj = UserProfile.objects.filter(forget_password_token = token).first()
        context = {'user_id' : profile_obj.user.id}
        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('reconfirm_password')
            user_id = request.POST.get('user_id')
            
            if user_id is  None:
                messages.success(request, 'No user id found.')
                return redirect(f'/change-password/{token}/')
                
            
            if  new_password != confirm_password:
                messages.success(request, 'both should  be equal.')
                return redirect(f'/change-password/{token}/')
                         
            
            user_obj = User.objects.get(id = user_id)
            user_obj.set_password(new_password)
            user_obj.save()
            return redirect('/login/')     
        
    except Exception as e:
        print(e)
    return render(request , 'change-password.html' , context)


import uuid
def ForgetPassword(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            
            if not User.objects.filter(username=username).first():
                messages.success(request, 'Not user found with this username.')
                return redirect('/forget-password/')
            
            user_obj = User.objects.get(username = username)
            token = str(uuid.uuid4())
            profile_obj= UserProfile.objects.get(user = user_obj)
            profile_obj.forget_password_token = token
            profile_obj.save()
            send_forget_password_mail(user_obj.email , token)
            messages.success(request, 'An email is sent.')
            return redirect('/forget-password/')                   
    except Exception as e:
        print(e)
    return render(request , 'forget-password.html')