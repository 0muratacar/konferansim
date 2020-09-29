from django.shortcuts import render,HttpResponse
from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect, render
from .forms import *
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_auth
from AdminPage.models import *

# Create your views here.

def index(request):
    return render(request,"anasayfa/index.html")


def userPageLaout(request):
    return render(request,"layouts/userPageLayout.html")

def hakemSayfası(request):
    return render(request,"kullanıcıSayfaları/hakemPage.html")

def editorSayfası(request):
    return render(request,"kullanıcıSayfaları/editorPage.html")

def yazarSayfası(request):
    return render(request,"kullanıcıSayfaları/yazarPage.html")



def giris(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            current_user_statu = request.user.statu
            if current_user_statu == 'editor':
                return render(request,'kullanıcıSayfaları/editorPage.html')
            elif current_user_statu == 'author':
                return render(request,'kullanıcıSayfaları/yazarPage.html')
            else:
                return render(request,'kullanıcıSayfaları/hakemPage.html')
            
        form = LoginForm()
        return render(request, "girisKaydol/login.html", {'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login_auth(request,user)
                return render(request,'kullanıcıSayfaları/yazarPage.html')
            else:
                form = LoginForm()
                return render(request, 'girisKaydol/login.html', {'ErrorMessage': 'Can Not Able To Authenticate You', 'form': form})
        else:
            form = LoginForm()
            return render(request, 'girisKaydol/login.html', {'ErrorMessage': 'Check Your Inputs', 'form': form})
  