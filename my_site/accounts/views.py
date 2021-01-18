from django.shortcuts import render,redirect
from django.views.generic import *
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse_lazy,reverse
from .forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import *
from django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model()
from my_site.settings import BASE_DIR

import os


# Create your views here.

class Homepage(TemplateView):
    template_name = 'index.html'



def register(request):

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm1(data=request.POST)


        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            messages.success(request, f'Account created for {user.username}!')
            return redirect('accounts:login')
        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm1()

    return render(request,'accounts/register.html',{'user_form':user_form,'profile_form':profile_form})


@login_required
def profile(request):
    if request.method == 'POST':
        pic2 =  str(request.user.profile.profile_pic.url)

        pic1 = pic2.replace("/","\\")
        pic = BASE_DIR + pic1

        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = UserProfileInfoForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            if pic == BASE_DIR + "\media\default.png" or pic2 == request.user.profile.profile_pic.url :
                pass
            else:
                os.remove(pic)
            return redirect('accounts:profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = UserProfileInfoForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'accounts/profile.html', context)




class TestPage(TemplateView):
    template_name = 'test.html'
class ContactPage(TemplateView):
    template_name = 'contact.html'
"""
class ThanksPage(TemplateView):
    template_name = 'thanks.html'
"""