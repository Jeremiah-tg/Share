from django import forms 
from .models import Post


# Styling the django framework forms with bootstrap
# specify the fields, use widgets and call the fields specfing the data types and class
class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ("title","title_tag","title_link","author","dead_line","body","header_image")
        widgets = {
            "title": forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            "title_tag": forms.TextInput(attrs={'class':'form-control','placeholder':'Event - Conference - Competition - Scholarships - Research - Price Award Events'}),
            "title_link": forms.TextInput(attrs={'class':'form-control','placeholder':'Use # if there`s no link'}),
            "author": forms.TextInput(attrs={'class':'form-control','value':'', 'id':'subscriber', 'type':'hidden'}),
            "dead_line": forms.DateInput(attrs={'class':'form-control','placeholder':'YYYY-mm-dd'}),
            # format=('%d-%m-%Y'),
            #   , 'type':'hidden'
            #    "author": forms.Select(attrs={'class':'form-control'}),
            "body": forms.Textarea(attrs={'class':'form-control','placeholder':'Describe the opportunity`s details here'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title","title_link","dead_line","body","header_image")
        widgets = {
            "title": forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            #  "title_tag": forms.TextInput(attrs={'class':'form-control','placeholder':'Event - Conference - Competition - Research - Price Award Events'}),
            "title_link": forms.TextInput(attrs={'class':'form-control','placeholder':'Use # if there`s no link'}),
            #    "author": forms.Select(attrs={'class':'form-control'}),
            "dead_line": forms.DateInput(attrs={'class':'form-control','placeholder':'YYYY-mm-dd'}),
            "body": forms.Textarea(attrs={'class':'form-control','placeholder':'Describe the opportunity`s details here'}),
        }