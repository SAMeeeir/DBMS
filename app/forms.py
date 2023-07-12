from django import forms
from .models import Student
import re


class PersonForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'

    ####validating the rollno 
    def clean_rollno(self):
        rollno = self.cleaned_data['rollno']
        introllno = rollno[-2:]
        pattern = re.compile(r'THA0(\d{2})(\w{3})0(\d{2})')

        if re.match(pattern, rollno) is None:
            raise forms.ValidationError('rollno must be in the format  THA077BEI038')
        elif introllno < '01' or introllno > '48':
            raise forms.ValidationError('rollno must be in between 01 and 48')
        return rollno

    ###validating the age
    def clean_age(self):
        age=self.cleaned_data['age']
        if age<1:
            raise forms.ValidationError('age cannot be negative or less then 0')
        return age
    