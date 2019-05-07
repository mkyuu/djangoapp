from django.contrib.auth import login
from django.shortcuts import render,redirect
from .forms import ProfileForm,UserCreateForm,LoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView,LogoutView
from django.views import generic


def regist_user(request):
    user_form = UserCreateForm(request.POST or None)
    profile_form = ProfileForm(request.POST or None)
    
    if request.method=='POST' and user_form.is_valid() and profile_form.is_valid():
        user = user_form.save(commit=False)
        user.is_active = True
        user.save()

        profile = profile_form.save(commit=False)
        profile.user = user
        profile.save()

        login(
            request,user,backend='django.contrib.auth.backends.ModelBackend'
        )

        return redirect('book_summary:index')

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request,'accounts/regist.html',context)


class Login(LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'

class Logout(LoginRequiredMixin,LogoutView):
    template_name = 'accounts/logout.html'