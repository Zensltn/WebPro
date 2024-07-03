from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import Tambah_jurusan,Edit_jurusan,Tambah_mahasiswa,Edit_mahasiswa,TambahDosen
from .models import jurusan,Mahasiswa,Dosen

# Create your views here.
def dashboard(request):
    return render(request,'dashboard.html')

def profil(request):
        return render(request,'profile.html')
    
def matakuliah(request):
        return render(request,'matakuliah.html')

def Jurusan(request):
        #SELECT * FROM jurusan
     Jurusan= jurusan.objects.all()
     
     context={
             'title':'DATA JURUSAN',
             'jurusan':Jurusan,    
                }
     return render(request,'jurusan.html',context)

def tambah_jurusan(request):
        if request.method == "POST":
                form= Tambah_jurusan(request.POST)
                if form.is_valid():
                   form.save()
                   messages.success(request,'Data Disimpan')
                   return redirect('manage_jurusan')
        else:
             form = Tambah_jurusan()
                        
        
        
        #form = Tambah_jurusan()
        
        context = {
                'title':'Form Tambah jurusan',
                'form':form,                
        }
        return render(request,'tambah_jurusan.html',context)

def edit_jurusan(request,jurusanid):
        Jurusan= jurusan.objects.get(id=jurusanid)
        
        if request.method == "POST":
                form = Edit_jurusan(request.POST,instance = Jurusan)
                if form.is_valid():
                   form.save()
                   messages.success(request,'Data Berhasil Diubah')
                   return redirect('manage_jurusan')
        else:
                form= Edit_jurusan(instance = Jurusan)
               
        context = {
                'title':'Form update jurusan',
                'form':form,                
        }
        return render(request,'edit_jurusan.html',context)

def hapus_jurusan(request,jurusanid):
        Jurusan= jurusan.objects.get(id=jurusanid)
        Jurusan.delete()
        messages.success(request,'Data Dihapus')
        return redirect('manage_jurusan')

def mahasiswa(request):
        mhs = Mahasiswa.objects.all()
        
        context ={
                'title':'DATA MAHASISWA',
                'mhs':mhs,
          }
        return render(request,'mahasiswa.html',context)
        
def tambah_mahasiswa(request):
        
        if request.method == 'POST':
                form =  Tambah_mahasiswa(request.POST)
                if form.is_valid():
                        form.save()
                        messages.success(request,'Data Mahasiswa Disimpan')
                        return redirect('manage_mahasiswa')
        else:
                form = Tambah_mahasiswa()
        
        context = {
                        'title':'TAMBAH MAHASISWA',
                        'form':form,
                }
        return render(request,'tambah_mahasiswa.html',context)
        
def edit_mahasiswa(request,mhsid):
        #editmhs =Mahasiswa.objects.get(id = mhsid)
        editmhs = Mahasiswa.objects.filter(id=mhsid).first()
        
        if request.method == 'POST':
                form =Edit_mahasiswa(request.POST,instance=editmhs)
                if form.is_valid():
                        form.save()
                        messages.success(request,"Data Mahasiswa Di ubah")
                        return redirect('manage_mahasiswa')
        else:
                form = Edit_mahasiswa(instance=editmhs)
                
        context={
                'title':'EDIT MAHASISWA',
                'form': form,
        }
        return render(request,'edit_mahasiswa.html',context)

def hapus_mahasiswa(request,mhsid):
        delmhs= Mahasiswa.objects.filter(id=mhsid).first()
        delmhs.delete()
        messages.success(request,'Data Dihapus')
        return redirect('manage_mahasiswa')

def dosen(request):
    dosen = Dosen.objects.all()
    
    context={
            'dosen':dosen,
    }
    return render(request,'dosen.html',context)

def tambah_dosen(request):
        if request.method =='POST':
                form = TambahDosen(request.POST,request.FILES)
                if form.is_valid():
                        form.save()
                        messages.success(request,'Data Dosen DIsimpan')
                        return redirect('manage_dosen')
        else:
                form=TambahDosen()
                
                context ={
                        'form':form,
                }
                return render(request,'tambah_dosen.html',context)
        
def viewdosen(request,dosenid):
        dosen= Dosen.objects.filter(id = dosenid).first()
        
        context={
                'dosen':dosen,
        }
        return render(request,'viewdosen.html',context)
