from django import forms  
import re
class StudentForm(forms.Form):
    # TODO: Define form fields here
    name = forms.CharField()
    mail_id = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    re_password = forms.CharField(widget=forms.PasswordInput)
    feedback = forms.CharField(widget=forms.Textarea)
    bot_handler = forms.CharField(required=False, widget=forms.HiddenInput)


    def clean(self):
    	print("validating tghe total form")
    	total_clean_data = super().clean()

    	input_name = total_clean_data['name']
    	if len(input_name)<3:
    		raise forms.ValidationError("name should be greater than 3 character")

    	input_feedback = total_clean_data['feedback']
    	if len(input_feedback)>50:
    		raise forms.ValidationError("feedback should be less than 50 character")


    	input_password = total_clean_data['password']
    	input_re_password= total_clean_data['re_password']

    	if input_password!=input_re_password:
    		raise forms.ValidationError("Password Missmatch!!!")

    	input_mail_id = total_clean_data['mail_id']
    	email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    	if not re.match(email_pattern,input_mail_id):
    		raise forms.ValidationError("enter valid email id")

    	input_bot_handler = total_clean_data['bot_handler']
    	if len(input_bot_handler)>0:
    		raise forms.ValidationError("Thanks BOT..... Do not try to automate you fool.....")






