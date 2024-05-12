from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import StudentForm,FilterStudents
from .models import Student
# Create your views here.

def home(request):
    #POST

    if request.method == "POST":
        form = StudentForm(request.POST)
        if(form.is_valid()):
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            course = form.cleaned_data["course"]
            gender = form.cleaned_data["gender"]
            age = form.cleaned_data["age"]

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
    filter = Student.objects.all()
    return render(request, 'student_table.html', {'filter':filter})

def student_table(request):
    student = Student.objects.all()
    return render(request,'student_table.html',{'student':student})

def delete(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect("/")

