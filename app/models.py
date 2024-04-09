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

    clg_course_name= models.TextField()
    clg_specialization= models.TextField(default=None)
    clg_name= models.TextField()
    clg_grading_system= models.TextField(choices=grading_choice)
    clg_grad=models.TextField()
    clg_duration_from= models.DateField(default='2000-01-01')
    clg_duration_to= models.DateField(default='2000-01-01')

    _10_school_name= models.TextField()
    _10_grading_system= models.TextField(choices=grading_choice)
    _10_grad=models.TextField()

    _12_school_name= models.TextField()
    _12_specialization= models.TextField(default=None)
    _12_grading_system= models.TextField(choices=grading_choice)
    _12_grad=models.TextField()
    

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