from django import forms 
import re 
class StudentForm(forms.Form):
    # TODO: Define form fields here
    name = forms.CharField()
    mail_id = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea)


    def clean_name(self):
    	input_name = self.cleaned_data['name']
    	print("validation of name field")

    	if len(input_name)<=3:
    		raise forms.ValidationError('the name should be more than 3 characters')

    	return input_name

    def clean_mail_id(self):
    	input_mailid = self.cleaned_data['mail_id']
    	print("validation of email field")

    	email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    	if not re.match(email_pattern, input_mailid):
    		raise forms.ValidationError('enter valid email address')
    	return input_mailid

    def clean_feedback(self):
    	input_feedback = self.cleaned_data['feedback']
    	print("validation for feedback")

    	if len(input_feedback)>50:
    		raise forms.ValidationError('the feedback should be less than 50 character')
    	return input_feedback
