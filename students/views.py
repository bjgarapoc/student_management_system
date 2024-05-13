from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import StudentForm, FilterForm
from .models import Student
from django.db.models import Q
# Create your views here.

def home(request):
    #POST
    if request.method == "POST":
        form = StudentForm(request.POST)
        if(form.is_valid()):
            student = Student(
                first_name = form.cleaned_data["first_name"],
                last_name = form.cleaned_data["last_name"],
                course = form.cleaned_data["course"],
                gender = form.cleaned_data["gender"],
                age = form.cleaned_data["age"]
            )
            student.save()
            return redirect("/")
        
    #GET
    context = {}
    context["form"] = StudentForm()
    return render(request,'student_form.html', context)

def filter_table(request):
    students = Student.objects.all()
    filter_form = FilterForm()
    context = {}

    # if request.method == "POST":
    #     filter_form = FilterForm(request.POST)
    #     if(filter_form.is_valid()):
    #         full_name = filter_form.cleaned_data("full_name")
    #         course = filter_form.cleaned_data("course")
    #         gender = filter_form.cleaned_data("gender")
    #         age_start = filter_form.cleaned_data("age_start")
    #         age_end = filter_form.cleaned_data("age_end")
            
    #         filter = Q()
    #         if full_name:
    #             filter &= Q(first_name__startswith=full_name) | Q(last_name__startswith=full_name)
    #         if course:
    #             filter &= Q(course=course)
    #         if gender:
    #             filter &= Q(gender=gender)
    #         if age_start and age_end:
    #             filter &= Q(age__range=(age_start,age_end))

    #         students = students.filter(filter)
    
    context["filter_form"] = FilterForm()
    # context = {'students':students,'filter_form': filter_form}
    return render(request,'student_table.html', context)

def student_table(request):
    student = Student.objects.all()
    return render(request,'student_table.html',{'student':student})

def delete(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect("/")
    
def update(request, id):
    context = {}
    student = Student.objects.get(id=id)
    
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student.first_name = form.cleaned_data["first_name"]
            student.last_name = form.cleaned_data["last_name"]
            student.course = form.cleaned_data["course"]
            student.gender = form.cleaned_data["gender"]
            student.age = form.cleaned_data["age"]
            student.save()
            return redirect("/")
    else:
        form = StudentForm(initial={
            'first_name': student.first_name,
            'last_name': student.last_name,
            'course': student.course,
            'gender': student.gender,
            'age': student.age
        })
    
    context["form"] = form
    return render(request, 'student_form.html', context)
