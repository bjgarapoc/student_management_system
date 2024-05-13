from django import forms

COURSES = (
    ("BS-CS", "Computer Science"),
    ("BS-DS", "Data Science"),
    ("BS-IT", "Information Technology"),
    ("BS-IS", "Information Systems")
)

GENDER = (
    ("FEMALE", "Female"),
    ("MALE", "Male")
)

class StudentForm(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    course = forms.ChoiceField(choices=COURSES, required=True)
    gender = forms.CharField(widget=forms.RadioSelect(choices=GENDER), required=True)
    age = forms.IntegerField(required=True)


class FilterForm(forms.Form):
    full_name = forms.CharField(required=False)
    course = forms.CharField(widget=forms.RadioSelect(choices=COURSES), required=False)
    gender = forms.CharField(widget=forms.RadioSelect(choices=GENDER), required=False)
    age_start = forms.IntegerField(required=False)
    age_end = forms.IntegerField(required=False)

