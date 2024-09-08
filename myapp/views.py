from django.shortcuts import render
from django.http import HttpResponse
from .models import Members
# Create your views here.
def members(request):
    members = Members.objects.all()
    return render(request,'members.html',{'members':members})