from django import forms 
from studentapp.models import StudentTable

class StudentTableForm(forms.ModelForm):
    class Meta:
        model = StudentTable
        fields = ('__all__')
