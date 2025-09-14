from django.shortcuts import render , redirect , reverse 
from .forms import SignUpForm , UserForm , ProfileForm
from django.contrib.auth import authenticate , login
from .models import Profile


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username , password=password)
            login(request , user)
            return redirect('/accounts/profile')
            
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


# profile page
def profile(request):
    profile = Profile.objects.get(user=request.user)
    
    if request.method == 'POST':
        userform = UserForm(request.POST,instance=request.user)
        profileform= ProfileForm(request.POST, request.FILES ,instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile=profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse('accounts:profile'))
    else:
        userform = UserForm(instance=request.user)
        profileform= ProfileForm(instance=profile)
    return render(request , 'accounts/profile.html' , {'profile' : profile , 'userform' : userform , 'profileform' : profileform})