from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/',views.profile , name='profile'),
    path(
    "reset_password/",
    auth_views.PasswordResetView.as_view(
        template_name="registration/password_reset.html",              
        email_template_name="registration/password_reset_email.html",  
        html_email_template_name="registration/password_reset_email.html"  
    ),
    name="reset_password",
),
]


