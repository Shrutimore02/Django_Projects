from django import forms  
import re
class StudentForm(forms.Form):
    # TODO: Define form fields here
    name = forms.CharField()
    mail_id = forms.EmailField()
    trainer_name = forms.CharField()
    feedback = forms.CharField(widget=forms.Textarea)

    def clean(self):
    	print('validation using single field method')
    	total_clean_data = super().clean()

    	input_name = total_clean_data['name']
    	if len(input_name)<=4:
    		raise forms.ValidationError("the name should be greater that 3 character")

    	input_trainer_name = total_clean_data['trainer_name']
    	if input_trainer_name[0].lower()!='s':
    		raise forms.ValidationError('the trainer name should starts with s|S')


    	input_feedback = total_clean_data['feedback']
    	if len(input_feedback)>=50:
    		raise forms.ValidationError("the feedback should be less that 50character")


    	input_mailid = total_clean_data['mail_id']
    	email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    	if not re.match(email_pattern, input_mailid):
    		raise forms.ValidationError("enter valid mail id")



