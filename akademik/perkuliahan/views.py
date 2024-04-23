from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dashboard(request):
    return render(request,'dashboard.html')

def profil(request):
        return render(request,'profile.html')
    
def matakuliah(request):
        return render(request,'matakuliah.html')

def mahasiswa(request):
        return render(request,'mahasiswa.html')

def Jurusan(request):
        return render(request,'jurusan.html')

def tambah_Jurusan(request):
        return render(request,'tambah_jurusan.html')