from django import forms 
class StudentForm(forms.Form):
	name = forms.CharField()
	password = forms.CharField()
	re_password = forms.CharField()
	trainer_name = forms.CharField()
	subject = forms.CharField()
	date = forms.DateField()
	mail_id = forms.EmailField()
	phone_number = forms.IntegerField()
	feedback = forms.CharField(widget=forms.Textarea)