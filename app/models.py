from django.db import models

# Create your models here.
class Student(models.Model):
   
    class AgeChoices(models.TextChoices):
        MALE='M','MALE'
        FEMALE='F','FEMALE'
        OTHER='O','OTHER'

    first_name=models.CharField(max_length=40)
    last_name=models.CharField(max_length=40)
    age=models.IntegerField()
    gender=models.CharField(max_length=10,choices=AgeChoices.choices)
    rollno=models.CharField(max_length=12,primary_key=True)
    department=models.CharField(max_length=30)

    def __str__(self):
        return f'{self.rollno}'

