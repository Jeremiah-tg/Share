from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from theblog.models import Profile

class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('campus_name','bio','profile_pic','linkedin_url','twitter_url','facebook_url','website_url','github_url','youtube_url')

        widgets ={
            "campus_name": forms.TextInput(attrs={'class':'form-control'}),
            "bio": forms.Textarea(attrs={'class':'form-control'}),
            # "profile_pic": forms.TextInput(attrs={'class':'form-control'}),
            "linkedin_url": forms.TextInput(attrs={'class':'form-control'}),
            "twitter_url": forms.TextInput(attrs={'class':'form-control'}),
            "facebook_url": forms.TextInput(attrs={'class':'form-control'}),
            "website_url": forms.TextInput(attrs={'class':'form-control'}),
            "github_url": forms.TextInput(attrs={'class':'form-control'}),
            "youtube_url": forms.TextInput(attrs={'class':'form-control'}),
        }


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':''}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email','password1', 'password2')

    # For the default registeration fields on how to apply bootstrap
    def __init__(self, *args, **kwargs): 
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] ='form-control'
        self.fields['password1'].widget.attrs['class'] ='form-control'
        self.fields['password2'].widget.attrs['class'] ='form-control'

class EditProfileForm(UserChangeForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    # is_staff = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'form-check'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email','password')
      
class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control','type':'password','placeholder':'Enter New Password'}))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control','type':'password','placeholder':'Confirm New Password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


