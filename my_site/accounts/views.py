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

from my_site.forms import ContactForm

import os


# Create your views here.

class Homepage(TemplateView):
    template_name = 'index.html'

def home(request):
    return render(request,'index.html',{})



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

"""
class TestPage(TemplateView):
    template_name = 'test.html'
class ContactPage(TemplateView):
    template_name = 'contact.html'
"""

"""
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template

def contact(request):
    form = form_class()
    if request.method == 'POST':
        form = form_class(data=request.POST)
        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')
            template = get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)
            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['youremail@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('home')
    return render(request, 'contact.html', {
        'form': form_class,
    })
"""

from django.core.mail import send_mail, BadHeaderError
    
def contactView(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            message = f'From: {from_email}\n' + message
            return_mail = {
                'subject': 'We received your mail',
                'message': 'Thank you for mailing us. Our team will get back to you soon.'
            }
            try:
                send_mail(subject, message, from_email, ['articults2020@gmail.com'])
                send_mail(return_mail['subject'], return_mail['message'], 'articults2020@gmail.com', [from_email])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('home')
    return render(request, "contact.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')