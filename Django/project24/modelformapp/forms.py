from modelformapp.models import StudentTable
from django import forms 

class StudentTableForm(forms.ModelForm):
	class Meta:
		model = StudentTable
		fields = ('__all__')
