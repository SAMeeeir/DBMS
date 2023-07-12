from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import PersonForm
from django.db import connection



#creating list as queryset
def createlist(rows):
    pass
    data = []
    for row in rows:
        item = {
            'first_name':row[0],
            'last_name':row[1],
            'age':row[2],
            'gender':row[3],
            'rollno':row[4],
            'department':row[5], 
        }
        data.append(item)
    return data
  

#extracting the data from the database
def extractdata():
    with connection.cursor() as cursor:
        cursor.execute('select *from app_student')
        rows=cursor.fetchall()
    data = []
    for row in rows:
        item = {
            'first_name':row[0],
            'last_name':row[1],
            'age':row[2],
            'gender':row[3],
            'rollno':row[4],
            'department':row[5], 
        }
        data.append(item)
    return data


def sortbyrollno():
    # data=extractdata()
    # sorted_students = sorted(data, key=lambda student: student['rollno'][-2:])
    # return sorted_students
    with connection.cursor() as cursor:
        cursor.execute('select *from app_student order by rollno')
        rows=cursor.fetchall()
    data=createlist(rows)
    return data




def sortbyname():
    # data=extractdata()
    # sorted_students = sorted(data, key=lambda student: student['first_name'])
    # return sorted_students
   with connection.cursor() as cursor:
        cursor.execute('select *from app_student order by first_name')
        rows=cursor.fetchall()
   data=createlist(rows)
   return data



def sortbyage():
    # data=extractdata()
    # sorted_students = sorted(data, key=lambda student: student['age'])
    # return sorted_students
    with connection.cursor() as cursor:
        cursor.execute("select *FROM app_student order by age")
        rows=cursor.fetchall()
    data=createlist(rows)
    return data

def onlyfemale():
    with connection.cursor() as cursor:
        cursor.execute("select *from app_student where gender='F'")
        rows=cursor.fetchall()
    data=createlist(rows)
    return data

def onlymale():
    with connection.cursor() as cursor:
        cursor.execute("select *from app_student where gender='M'")
        rows=cursor.fetchall()
    data=createlist(rows)
    return data



def home(request):
    form = PersonForm()
    #entering the data in database if request method is post
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']
            rollno = form.cleaned_data['rollno']
            department = form.cleaned_data['department']

            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO app_student (first_name, last_name, age, gender, rollno, department) "
                    "VALUES (%s, %s, %s, %s, %s, %s)",
                    [first_name, last_name, age, gender, rollno, department]
                )

            return redirect('/home')
    
    #for sorting according to user request
    if request.GET.get('sort')=='name':
        data=sortbyname()
    elif request.GET.get('sort')=='rollno':
        data=sortbyrollno()
    elif request.GET.get('sort')=='age':
        data=sortbyage()
    elif request.GET.get('sort')=='female':
        data=onlyfemale()
    elif request.GET.get('sort')=='male':
        data=onlymale()
    else:
        data=extractdata()
  
    return render(request, 'app/index.html', {'form': form,'data':data})




def delete(request, id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM app_student WHERE rollno = %s", [id])
    return redirect('/home')



def deleteall(request):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM app_student")
    return redirect('/home')


