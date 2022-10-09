from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView,DetailView, CreateView
from django.contrib.auth import login,logout
from .forms import *
from .models import *
from django.db.models import Count

class WatchList(ListView):
    paginate_by = 2
    model = Film
    context_object_name = 'films'
    template_name ='Film/search.html'


    def get_paginate_by(self, queryset):
        return self.request.GET.get("paginate_by", self.paginate_by)


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


def search_category(request, category_id):

    films = Film.objects.filter(category=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)

    context = {

        'films': films,
        'categories': categories,

    }
    return render(request, template_name='Film/category.html', context=context)


def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
        new_user.set_password(user_form.cleaned_data['password1'])
        new_user.save()
        return render(request, 'Film/All_about_user/Register_done.html',context={'new_user': new_user})

    else:
        user_form = UserRegisterForm()
    return render(request, 'Film/All_about_user/Register.html',{'user_form':user_form})

def LogoutUser(request):
    logout(request)
    return redirect('Home')


def LoginUser(request):
    if request.method=='POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('Home')
    else:
        form =UserLoginForm()
    return render(request,'Film/All_about_user/Login.html',context={'user_form':form})




def Ss(request):
    film = Film.objects.all()
    return render(request,'Film/Main/index.html')

def wotch(request):
    films = Film.objects.all()
    categories = Category.objects.all()
    return render(request, 'Film/search.html', context={'films':films,'categories' : categories,})

class Home(ListView):
    model = Film
    template_name = 'Film/Main/index.html'
    context_object_name = 'film'

def watch(request,film_id):
    films = Film.objects.get(pk=film_id)
    return render(request, 'Film/watch.html', context={'films': films})




