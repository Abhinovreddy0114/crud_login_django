from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator


@login_required(login_url='/login/')
def receipes(request):
    if request.method == 'POST':
        receipe_image = request.FILES.get("receipe_image")
        receipe_name = request.POST.get("receipe_name")
        receipe_description = request.POST.get("receipe_description")
        Receipe.objects.create(receipe_image=receipe_image,receipe_name=receipe_name,receipe_description=receipe_description)
    queryset = Receipe.objects.all()
    context = {'receipes':queryset}
    return render(request,'receipes.html',context)


@login_required(login_url='/login/')
def delete_receipe(request,id):
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    return redirect('/receipes/')


@login_required(login_url='/login/')
def update_receipe(request, id):
    queryset = Receipe.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        receipe_image = request.FILES.get('receipe_image') 
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description

        if receipe_image:
            queryset.receipe_image = receipe_image

        queryset.save()
        return redirect("/receipes/")
    
    context = {'receipe': queryset}
    return render(request, 'update.html', context)


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not User.objects.filter(username=username).exists:
            return redirect('/login/')
        user = authenticate(username=username,password=password)
        if user is None:
            return redirect('/login/')
        print(f'Authenticated user:{user.username}')
        login(request,user)
        return redirect('/receipes/')
    return render(request,'login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not all([first_name, last_name, username, password]):
            return redirect('/register/')
        if User.objects.filter(username=username).exists():
            return redirect('/register/')
        user = User.objects.create(
            first_name=first_name, 
            last_name=last_name,
            username=username
        )
        user.set_password(password)
        user.save()  
        return redirect('/login/')
    return render(request, 'register.html')