from django.db import models

# Create your models here.

class subject(models.Model):
    subjectname=models.CharField(unique=True,max_length=50,null=False)

class user(models.Model):
    
    name=models.CharField(max_length=100,null=False)
    email=models.EmailField(null=False,unique=True)
    profession=models.CharField(null=False)
    subject_id=models.ManyToManyField(subject,null=True,default="3",related_name="sub")


class marks(models.Model):
    subjectmarks=models.DecimalField(max_digits=100,decimal_places=2)
    subject_id=models.ForeignKey(subject,null=False,on_delete=models.CASCADE,related_name="subject")
    student_id=models.ForeignKey(user,null=False,on_delete=models.CASCADE,related_name="student")




