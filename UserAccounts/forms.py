# forms.py
from django import forms
from .models import PostJobData
from .models import UserComment

class DataForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Name', 'id': 'subject', 'required':True}))
    job_title = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Job Title', 'id': 'subject', 'required':True}))
    job_location = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Job Location', 'id': 'subject', 'required':True}))
    job_des = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Job Description', 'id': 'subject', 'required':True}))
    job_image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = PostJobData
        fields = ['name', 'job_title', 'job_location', 'job_des', 'job_image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = UserComment
        fields = ('text',)
        widgets = {
            'text' : forms.Textarea(attrs={'class' : 'form-control'}),
        }

