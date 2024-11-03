from django import forms  
from django.core import validators

def trainer_name(data):
	if data[0].lower()!='s':
		raise forms.ValidationError('Trainer name should be start with s|S')

class StudentForm(forms.Form):
    # TODO: Define form fields here
    name = forms.CharField()
    mail_id = forms.EmailField()
    trainer_name = forms.CharField(validators=[trainer_name])
    feedback = forms.CharField(widget=forms.Textarea)

