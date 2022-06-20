from django.db import models

# Create your models here.

class userSignup(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=12)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    mobile=models.BigIntegerField()

class notes(models.Model):
    qtitle=models.CharField(max_length=100)
    tech=models.CharField(max_length=100)
    myfile=models.FileField(upload_to='NotesUpload')
    comments=models.TextField()

class feedback(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.BigIntegerField()
    msg=models.TextField()