from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .forms import SignUp, FormEdit, ProfilePageForm
from theBlog.models import Profile

# Create your views here.

class CreateProfile(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_profile.html'
    #fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditProfilePage(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio','profile_pic','website_url','email_url','facebook_url','twitter_url','reddit_url']
    success_url = reverse_lazy('home')

class ChangePasswords(PasswordChangeView):
    form_class= PasswordChangeForm
    success_url = reverse_lazy('home')


class UserRegister(generic.CreateView):
    form_class = SignUp
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEdit(generic.UpdateView):
    form_class = FormEdit
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')
    
    def get_object(self):
        return self.request.user