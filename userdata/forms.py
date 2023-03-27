from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from theBlog.models import Profile


class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'website_url', 'email_url', 'facebook_url', 'twitter_url', 'reddit_url')

        widgets = {
            'bio': forms.Textarea(attrs={'class':'form-control'}),
            'website_url': forms.TextInput(attrs={'class':'form-control'}),
            'email_url': forms.TextInput(attrs={'class':'form-control'}),
            'facebook_url': forms.TextInput(attrs={'class':'form-control'}),
            'twitter_url': forms.TextInput(attrs={'class':'form-control'}),
            'reddit_url': forms.TextInput(attrs={'class':'form-control'}),
        }

class SignUp(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'})),
    display_name = forms.CharField(max_length=18, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username','display_name','email','password1','password2')

    def __init__(self,*args,**kwargs):
        super(SignUp,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class FormEdit(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'})),
    display_name = forms.CharField(max_length=18, widget=forms.TextInput(attrs={'class':'form-control'})),
    first_name = forms.CharField(max_length=18, widget=forms.TextInput(attrs={'class':'form-control'})),
    last_name = forms.CharField(max_length=18, widget=forms.TextInput(attrs={'class':'form-control'})),
    username = forms.CharField(max_length=18, widget=forms.TextInput(attrs={'class':'form-control'})),
    last_login = forms.CharField(max_length=18, widget=forms.CheckboxInput(attrs={'class':'form-check'})),
    is_superuser = forms.CharField(max_length=18, widget=forms.CheckboxInput(attrs={'class':'form-check'})),
    is_staff = forms.CharField(max_length=18, widget=forms.CheckboxInput(attrs={'class':'form-check'})),
    is_active = forms.CharField(max_length=18, widget=forms.CheckboxInput(attrs={'class':'form-check'})),
    date_joined = forms.CharField(max_length=18, widget=forms.TextInput(attrs={'class':'form-control'})),

    class Meta:
        model = User
        fields = ('username','email','first_name','last_name')
        
