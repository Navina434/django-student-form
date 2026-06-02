from django import forms
from .models import Student
import re

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['name', 'email', 'age']

    def clean_name(self):
        name = self.cleaned_data['name']

        if not re.match(r'^[A-Za-z ]+$', name):
            raise forms.ValidationError(
                "Name should contain only letters."
            )

        return name

    def clean_age(self):
        age = self.cleaned_data['age']

        if age <= 18:
            raise forms.ValidationError(
                "Age must be greater than 18."
            )

        return age