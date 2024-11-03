from django import forms 
class Cricketer(forms.Form):
	name = forms.CharField(max_length=50)
	age = forms.IntegerField()
	city = forms.CharField(max_length=20)
	role = forms.CharField(max_length=15)
	dob = forms.DateField()
	jersey_no = forms.IntegerField()