from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'dummy_login/login.html')

def Register(request):
    return render(request,'dummy_login/Register.html')