from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from .models import Password

def get_passwords(request):
    password_list = Password.objects.all()
    context = {'password_list': password_list}
    
    return render(request, 'passwords/index.html', context)
