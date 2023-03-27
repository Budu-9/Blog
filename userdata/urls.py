from django.urls import path
from .views import UserRegister, UserEdit, ChangePasswords, EditProfilePage, CreateProfile
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', UserRegister.as_view(), name = 'register'),
    path('edit_profile/', UserEdit.as_view(), name = 'edit_profile'),
    path('password/', ChangePasswords.as_view(template_name='registration/change-password.html')),
    path('<int:pk>/edit_profile/', EditProfilePage.as_view(), name = 'edit_profile_page'),
    path('create_profile/', CreateProfile.as_view(), name = 'create_profile'),
]