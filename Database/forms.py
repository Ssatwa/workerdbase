# register the form entries here

from django import forms
from Database.models import Worker

class Workerform(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ['firstname','lastname','email','dob','education']