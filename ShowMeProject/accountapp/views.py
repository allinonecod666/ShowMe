from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth import settings
from pip._vendor.requests import request

from .extra_fun import send_sms, gen_otp

account_sid = 'ACf009d625ed8ae87dda1842faec3a76fa'
auth_token = '67d2e2d96ca54cb692ff6066bf533922'
random_otp = gen_otp()


def register_fun(request):
    if request.method == 'POST':
        form_usr = UserCreationForm(request.POST)
        if form_usr.is_valid():
            print('this is fucking post man!')
            usr = form_usr.save()
            u_phn = form_usr.cleaned_data['username']
            print('form is saved but phon isnt')
            msg_body = f'''

            Welcome To WATCH-ME

            Thank You For Joining In Watch-Me Video's
            Shering Site,ACTIVATE YOUR ACCOUNT
            your secret digit : {random_otp}click hear to submit otp : http://192.168.1.3:8000/Account/activate?phone={request.user.username}&code={random_otp}'''

            send_sms(account_sid, auth_token, msg_body, '+13236732893', u_phn)
            print('msg send successed')
            login(request, usr)
            return redirect('/')
    else:
        form_usr = UserCreationForm()
    context = {
        'form_usr': form_usr,
    }
    return render(request, 'accountapp/register.html', context)


def login_fun(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        print('post')
        if form.is_valid():
            print('valid')
            login(request, form.get_user())
            print('logedin')
            return redirect('/')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accountapp/login.html', context)


def logout_fun(request):
    logout(request)
    return redirect('login')


def profile_fun(request):
    try:
        rusr = request.user
    except:
        rusr = ''

    context = {
        'rusr': rusr,

    }

    return render(request, 'accountapp/profile.html')

def activate_fun(request):
    phone = request.GET.get('phone')
    code = request.GET.get('code')
    context = {
        'code': code,
    }
    return render(request, 'accountapp/activate.html', context)
