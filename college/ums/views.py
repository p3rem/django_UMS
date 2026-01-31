from django.shortcuts import render, redirect
from django.http import HttpResponse
from ums.models import Student, about as AboutModel, contact as ContactModel

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    aboutusinfo = AboutModel.objects.all()
    return render(request, 'about.html', {'aboutusinfo': aboutusinfo})

def add_about(request):
    if request.method == 'GET':
        cname = request.GET.get('cname')
        location = request.GET.get('location')
        established_year = request.GET.get('established_year')
        mission = request.GET.get('mission')
        vision = request.GET.get('vision')
        
        if cname and location and mission and vision:
            ab = AboutModel(
                cname=cname,
                location=location,
                established_year=established_year,
                mission=mission,
                vision=vision
            )
            ab.save()
            return redirect('about')
    
    return render(request, 'add_about.html')

def edit_about(request, id):
    ab = AboutModel.objects.get(id=id)
    if request.method == 'GET':
        cname = request.GET.get('cname')
        location = request.GET.get('location')
        established_year = request.GET.get('established_year')
        mission = request.GET.get('mission')
        vision = request.GET.get('vision')
        
        if cname or location or mission or vision:
            if cname:
                ab.cname = cname
            if location:
                ab.location = location
            if established_year:
                ab.established_year = established_year
            if mission:
                ab.mission = mission
            if vision:
                ab.vision = vision
            ab.save()
            return redirect('about')
    
    return render(request, 'edit_about.html', {'about': ab})

def delete_about(request, id):
    ab = AboutModel.objects.get(id=id)
    ab.delete()
    return redirect('about')

def contact(request):
    if request.method == 'GET':
        name = request.GET.get('name')
        email = request.GET.get('email')
        message = request.GET.get('message')
        
        if name and email and message:
            ct = ContactModel(
                address=name,
                phone_number=email,
                email=email,
                message=message
            )
            ct.save()
            return redirect('view_contact')
    
    contactusinfo = ContactModel.objects.all()
    return render(request, 'conatct.html', {'contactusinfo': contactusinfo})

def view_contact(request):
    contactusinfo = ContactModel.objects.all()
    return render(request, 'view_contact.html', {'contactusinfo': contactusinfo})

def register(request):
    return render(request, 'register.html')

def student_entry(request):
    if request.method == 'GET':

        name = request.GET.get('b1')
        email = request.GET.get('b2')
        enrollment_date = request.GET.get('b3')
        dept = request.GET.get('b4')
        phno = request.GET.get('b5')
        
        if name and email and dept and phno:
            student = Student(
                name=name,
                email=email,
                dept=dept,
                phno=phno
            )
            student.save()
            return HttpResponse("Student registered successfully!")
        
    return render(request, 'register.html')

def student(request):
    u = Student.objects.all()
    return render(request, 'student.html', {'u': u})