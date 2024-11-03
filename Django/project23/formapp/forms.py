from django import forms
class EmployeeData(forms.Form):
	name = forms.CharField()
	address = forms.CharField()
	salary = forms.IntegerField()
	mail_id = forms.EmailField()
	phone_number = forms.IntegerField()