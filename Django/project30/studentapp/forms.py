from django import forms 
from django.core  import validators
from django.core.validators  import EmailValidator
class StudentForm(forms.Form):
    # TODO: Define form fields here
    name = forms.CharField(validators = [validators.MinLengthValidator(3), validators.MaxLengthValidator(20)])
    mai_id = forms.EmailField(validators=[EmailValidator()])
    feedback = forms.CharField(widget = forms.Textarea,  validators=[validators.MaxLengthValidator(50)])
