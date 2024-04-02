from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dashboard(request):
    return render(request,'dashboard.html')

def profil(request):
        return render(request,'profile.html')
    
def matakuliah(request):
        return render(request,'matakuliah.html')
