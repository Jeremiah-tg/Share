from django.shortcuts import render, get_object_or_404
from django.views import generic 
from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm, ProfilePageForm
from django.contrib import messages
from theblog.models import Profile

class CreateProfilePageView(CreateView):
    model= Profile
    form_class = ProfilePageForm
    template_name = "registration/create_user_profile_page.html"
    # fields = '__all__'

# making the form being created be saved under a right user.
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name ='registration/edit_profile_page.html'
    fields =['bio','campus_name','profile_pic','linkedin_url','twitter_url','facebook_url','website_url','github_url','youtube_url'] 
    
    success_url = reverse_lazy('home')


class ShowProfilePageView(DetailView):
    model = Profile
    template_name="registration/user_profile.html"
    def get_context_data(self, *args, **kwargs):
        user = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context = super().get_context_data(**kwargs)
        context["page_user"] = page_user
        return context
        


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    # form_class =PasswordChangeForm
    success_url = reverse_lazy('password_sucess')
    # success_url = reverse_lazy('home') #when it is successful, it redirects to a home page

def password_success(request):
    return render(request,'registration/password_success.html',{})


# Create your views here.
class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = "registration/register.html"
    # success_url = reverse_lazy('login') #when it is successful, it redirects to a login page
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = "registration/edit_profile.html"
    success_url = reverse_lazy('home') #when it is successful, it redirects to a home page

    def get_object(self):
        return self.request.user