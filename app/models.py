from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model



class Additionally_Filed_User(AbstractUser):
    user_choice=(
        ('Seeker','Seeker'),
        ('Company', 'Company')
    )
    user_type= models.TextField(choices=user_choice)

User= get_user_model()

class Seeker_Personal_Information(models.Model):

    gender_choice=(
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),
    )
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    dob=models.DateField(default='2000-01-01')
    gender=models.TextField(choices=gender_choice)
    curr_addr=models.TextField(default="India")
    addr=models.TextField(default="India")
    gender=models.TextField(choices=gender_choice)
    contact=models.PositiveIntegerField()
    profile_pic=models.ImageField(upload_to='profile images/',)

    def __str__(self) -> str:
        return self.user.username
    
    
class Seeker_Education(models.Model):


    user=models.ForeignKey(User, on_delete=models.CASCADE)
    grading_choice=(
        ('Percentage','Percentage'),
        ('GPA','GPA')
    )
    
    clg_specialization_choice=(
            
            ('Data Science','Data Science'),
            ('Cybersecurity','Cybersecurity'),
            ('Web Development','Web Development'),
            ('Biomedical Engineering','Biomedical Engineering'),
            ('Biology','Biology'),
            ('Mathematics','Mathematics'),
            ('Electrical Engineering','Electrical Engineering'),
            ('Other','Other'),

    )
    st_12_specialization_choice=(

        ('Mathematics','Mathematics'),
        ('Biology','Biology'),
        ('Commerce','Commerce'),
        ('Arts','Arts'),
    )

    clg_course_name= models.TextField()
    clg_specialization= models.TextField(default=None,choices=clg_specialization_choice)
    clg_name= models.TextField()
    clg_grading_system= models.TextField(choices=grading_choice)
    clg_grad=models.TextField()
    clg_duration_from= models.DateField(default='2000-01-01')
    clg_duration_to= models.DateField(default='2000-01-01')

    st_10_school_name= models.TextField()
    st_10_grading_system= models.TextField(choices=grading_choice)
    st_10_grad=models.TextField()

    st_12_school_name= models.TextField()
    st_12_specialization= models.TextField(default=None,choices=st_12_specialization_choice)
    st_12_grading_system= models.TextField(choices=grading_choice)
    st_12_grad=models.TextField()
    

    def __str__(self) -> str:
        return self.user.username
    
class Seeker_Professional_Information(models.Model):

    notice_period_choice =(
        ('Immediate','Immediate'),
        ('Less then 15','Less then 15'),
        ('1 Month','1 Month'),
        ('2 Month','2 Month'),
        ('More Then 2 Month','More Then 2 Month'),
    )

    experience_level_choices=(
        ('Fresher','Fresher'),
        ('6 Month','6 Month'),
        ('1 Year+','1 Year+'),
        ('3 Year+','3 Year+'),
        ('More then 5','More then 5'),

    )

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    desc= models.TextField()
    notice_period= models.TextField(choices=notice_period_choice)
    key_skill=models.TextField()
    project=models.TextField()
    experience_level=models.TextField(choices=experience_level_choices)
    cv=models.FileField(upload_to='resums/',)

    
    def __str__(self) -> str:
        return self.user.username
    
class Comapny_Profile(models.Model):

    company_category_choice=(
        ('Education','Education'),
        ('Pharmaceutical','Pharmaceutical'),
        ('Information Technology (IT)','Information Technology (IT)'),
        ('Finance and Banking','Finance and Banking'),
        ('Consulting and Professional Services','Consulting and Professional Services'),
        ('Other','Other'),

    )

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    c_logo=models.ImageField(upload_to="company_logo/")
    cname=models.TextField()
    company_contact=models.TextField()
    company_category=models.TextField(choices=company_category_choice)
    c_desc=models.TextField()
    c_link=models.URLField(max_length=200)
    c_addr=models.TextField()
    country_name=models.TextField()

    def __str__(self) -> str:
        return self.user.username