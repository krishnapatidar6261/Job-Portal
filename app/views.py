from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.hashers import make_password,check_password
from django.conf import settings
from django.core.mail import send_mail
import random
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from . models import *

#we use Additionally Filed so we need to import and naming as usermodel
User = get_user_model()


def index(request):

    return render(request,'index.html')

def about(request):

    return render(request,'about.html')

def blog(request):

    return render(request,'blog.html')

def contact(request):

    return render(request,'contact.html')


def register(request):
    
    if request.method =="POST":
        
        username= request.POST.get('email')
        email= request.POST.get('email')
        user_type= request.POST.get('user_type')
        fname= request.POST.get('fname')
        lname= request.POST.get('lname')
        pwd= request.POST.get('pwd')
        cpwd= request.POST.get('cpwd')

        if User.objects.filter(username = username, email=email).exists():
            msg= "User Already Register Please Login"
            return render(request, 'login.html',{'msg':msg})
        
        if pwd == cpwd:
            User.objects.create(

                username =username,
                email =email,
                first_name =fname,
                last_name=  lname,
                user_type = user_type,
                password=  make_password(pwd)
            )

            msg="Register Successfully"

            return render(request, 'login.html',{'msg':msg})
        
        else:
            msg="Password & Confirm Password Does Not Match"
            print(msg)
            return render(request,'register.html',{'msg':msg})
        
    return render(request, 'register.html')

def login(request):
    if request.method == "POST":
        email=request.POST.get('email')
        pwd= request.POST.get("pwd")

        user = authenticate(request, username= email, password=pwd)
        if user is None:
            msg="Invalid Login Crediantial"

            return render(request, 'login.html',{"msg": msg})
        
        else:
            auth_login(request,user)
            if user.user_type=="Seeker":
                user_instance=User.objects.get(email=request.user)

                if not Seeker_Personal_Information.objects.filter(user=user_instance).exists():
                    
                    return render(request,'seeker-profile-create.html',{'user': user})
                
                return render(request,'index.html')
            
            elif user.user_type == "Company":
                user_instance=User.objects.get(email=request.user)
                
                if not Comapny_Profile.objects.filter(user=user).exists():
                    return render(request,'company-profile-create.html')
                
                return render(request, 'index.html')
            
            return render(request, 'index.html')

    return render(request, 'login.html')


def logout(request):
    
    auth_logout(request)

    return redirect('login')

def forgot_password(request):

    if request.method =="POST":

        email=request.POST.get('email')
        user=User.objects.filter(username=email)

        if user.exists():
            #filter return a more then one data so we need to change into single
            #first() return a first value from the query set
            user_instance = user.first()
            subject = 'Job Portal Forgot Password'
            otp=random.randint(1000,9999)
            message = f'Hello {user_instance.first_name}, Your Forgot Password Otp is {otp}.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email,]
            send_mail( subject, message, email_from, recipient_list )

            msg="Otp Sent on Email"

            return render(request,"verify-otp.html",{'msg':msg,'email': email,'otp':otp})

        else:
            msg="Email Not Register"
            return render(request, 'forgot-password.html',{'msg':msg})
    
    return render(request, 'forgot-password.html')

def verify_otp(request):
    
    if request.method=="POST":

        email=request.POST.get('email')
        otp=request.POST.get('otp')
        user_otp=request.POST.get('user_otp')
        print("otp",otp)
        print("email",email)
        print(user_otp)
        if otp == user_otp:
            
            return render(request,'new-password.html',{'email': email})
            
        msg="Otp Does Not Matched"
        return render(request,'verify-otp.html',{'msg':msg,'email': email,'otp':otp})
    
    return render(request,'verify-otp.html')

def new_password(request):

    if request.method == "POST":

        email=request.POST.get('email')
        pwd=request.POST.get('pwd')
        cpwd=request.POST.get('cpwd')

        if pwd == cpwd:
            
            user=get_object_or_404(User, username=email)

            user.password = make_password(pwd)
            user.save()
            msg="Password Reset Successfully"
            return render(request,'login.html',{'msg': msg})

        else:
            msg="Password & Confirm Password Does Not Match"
            return render(request,'new-password.html',{'msg':msg, 'email':email})

    return render(request,'new-password.html')

@login_required(login_url='/login/')
def change_password(request):
    
    if request.method == "POST":

        old_pwd= request.POST.get('old_pwd')
        new_pwd= request.POST.get('pwd')
        cpwd=request.POST.get('cpwd')

        user=User.objects.get(username=request.user)
        print(user.password)
        print(old_pwd)

        if user.check_password(old_pwd):
            if new_pwd == cpwd:

                user.set_password(new_pwd)
                user.save()

                msg="Password Changed"
                return render(request,'login.html',{'msg':msg})
            else:
                msg="Password and Confirm Password Does Not Matched"
                return render(request, 'change-password.html',{'msg':msg})
        else:
            msg="Old Password Does Not Matched"
            return render(request, 'change-password.html',{'msg':msg})
        
    return render(request, 'change-password.html')

@login_required(login_url='/login/')
def profile_create(request):
    
    user=User.objects.get(email=request.user)
    if user.user_type == "Seeker":
        if request.method == "POST":
        #professional Summary Field
            desc= request.POST.get('desc')
            notice_period= request.POST.get('notice_period')
            key_skill= request.POST.get('key_skill')
            project= request.POST.get('project')
            experience_level= request.POST.get('experience_level')
            cv= request.FILES.get('cv')

            #Education Detail
            clg_course_name= request.POST.get('clg_course_name')
            clg_specialization= request.POST.get('clg_specialization')
            clg_name= request.POST.get('clg_name')
            clg_grading_system= request.POST.get('clg_grading_system')
            clg_grad= request.POST.get('clg_grad')
            clg_duration_from= request.POST.get('clg_duration_from')
            clg_duration_to= request.POST.get('clg_duration_to')
            _10_school_name= request.POST.get('_10_school_name')
            _10_grading_system= request.POST.get('_10_grading_system')
            _10_grad= request.POST.get('_10_grad')
            _12_school_name= request.POST.get('_12_school_name')
            _12_specialization= request.POST.get('_12_specialization')
            _12_grading_system= request.POST.get('_12_grading_system')
            _12_grad= request.POST.get('_12_grad')

            #Personal Detail
            dob=request.POST.get('dob')
            gender=request.POST.get('gender')
            contact=request.POST.get('contact')
            profile_pic=request.FILES.get('profile_pic')
            addr=request.POST.get('addr')
            curr_addr=request.POST.get('curr_addr')


            Seeker_Personal_Information.objects.create(
                user=user,
                dob=dob,
                gender=gender,
                contact=contact,
                profile_pic=profile_pic,
                addr=addr,
                curr_addr=curr_addr
            )

            Seeker_Education.objects.create(
                user=user,
                clg_course_name=clg_course_name,
                clg_specialization=clg_specialization,
                clg_name=clg_name,
                clg_grading_system=clg_grading_system,
                clg_grad=clg_grad,
                clg_duration_from=clg_duration_from,
                clg_duration_to=clg_duration_to,
                st_10_school_name=_10_school_name,
                st_10_grading_system=_10_grading_system,
                st_10_grad=_10_grad,
                st_12_school_name=_12_school_name,
                st_12_specialization=_12_specialization,
                st_12_grading_system=_12_grading_system,
                st_12_grad=_12_grad,

            )
            Seeker_Professional_Information.objects.create(
                user=user,
                desc= desc,
                notice_period= notice_period,
                key_skill= key_skill,
                project= project,
                experience_level= experience_level,
                cv= cv,
            )

            return render(request,'index.html')
        
        return render(request, 'seeker-profile-create.html')
    
    elif user.user_type == "Company":

        if request.method == "POST":
            print(request.POST.get('cname'))
            Comapny_Profile.objects.create(

                user = user,
                c_logo = request.FILES.get('c_logo'),
                cname = request.POST.get('cname'),
                company_contact = request.POST.get('company_contact'),
                company_category = request.POST.get('company_category'),
                c_desc = request.POST.get('c_desc'),
                c_link = request.POST.get('c_link'),
                c_addr = request.POST.get('c_addr'),
                country_name = request.POST.get('country_name'),
            )

            return render(request,'index.html')

        return render(request,'company-profile-create.html')
    
@login_required(login_url="/login/")   
def profile(request):
    
    user=User.objects.get(email=request.user)
    
    if user.user_type =="Seeker":
        #check filed is created or not
        if not Seeker_Personal_Information.objects.filter(user=user).exists():
            return render(request, 'seeker-profile-create.html')

        personal_info=Seeker_Personal_Information.objects.get(user=user)
        professional_info=Seeker_Professional_Information.objects.get(user=user)
        education_info=Seeker_Education.objects.get(user=user)

        if request.method == "POST":
            
            cv= request.FILES.get('cv')
            profile_pic=request.FILES.get('profile_pic')
            personal_info.dob=request.POST.get('dob')
            personal_info.gender=request.POST.get('gender')
            personal_info.contact=request.POST.get('contact')
            personal_info.addr=request.POST.get('addr')
            personal_info.curr_addr=request.POST.get('curr_addr')

            if profile_pic is not None:
            
                personal_info.profile_pic=profile_pic
            personal_info.save()
            #update education detail
            education_info.clg_course_name=request.POST.get('clg_course_name')
            education_info.clg_specialization=request.POST.get('clg_specialization')
            education_info.clg_name=request.POST.get('clg_name')
            education_info.clg_grading_system=request.POST.get('clg_grading_system')
            education_info.clg_grad=request.POST.get('clg_grad')
            education_info.clg_duration_from=request.POST.get('clg_duration_from')
            education_info.clg_duration_to=request.POST.get('clg_duration_to')
            education_info.st_10_school_name=request.POST.get('_10_school_name')
            education_info.st_10_grading_system=request.POST.get('_10_grading_system')
            education_info.st_10_grad=request.POST.get('_10_grad')
            education_info.st_12_school_name=request.POST.get('_12_school_name')
            education_info.st_12_specialization=request.POST.get('_12_specialization')
            education_info.st_12_grading_system=request.POST.get('_12_grading_system')
            education_info.st_12_grad=request.POST.get('_12_grad')
            education_info.save()
            # profession information update
            professional_info.desc=request.POST.get('desc')
            professional_info.notice_period=request.POST.get('notice_period')
            professional_info.key_skill=request.POST.get('key_skill')
            professional_info.project=request.POST.get('project')
            professional_info.experience_level=request.POST.get('experience_level')
            if cv is not None:
            
                professional_info.cv= cv
            professional_info.save()
            msg="Profile Update Successfully"
            data={  'personal_info':personal_info,
                    'professional_info':professional_info,
                    'education_info':education_info,
                    'msg': msg}
            return render(request,'seeker-profile.html',data)

    
        data={  'personal_info':personal_info,
                'professional_info':professional_info,
                'education_info':education_info,
                }

        return render(request,'seeker-profile.html',data)
    
    elif user.user_type =="Company":
        
        if not Comapny_Profile.objects.filter(user=user).exists():

            return render(request,'company-profile-create.html')
        
        comp_prof=Comapny_Profile.objects.get(user=user)

        if request.method == "POST":

            c_logo = request.FILES.get('c_logo')
            
           
            comp_prof.cname = request.POST.get('cname')
            comp_prof.company_contact = request.POST.get('company_contact')
            comp_prof.company_category = request.POST.get('company_category')
            comp_prof.c_desc = request.POST.get('c_desc')
            comp_prof.c_link = request.POST.get('c_link')
            comp_prof.c_addr = request.POST.get('c_addr')
            comp_prof.country_name = request.POST.get('country_name')

            if c_logo is not None:
                comp_prof.c_logo = c_logo
            
            print("exceute")
            return render(request,'index.html')

        
        return render(request,"company-profile.html",{'comp_prof':comp_prof})