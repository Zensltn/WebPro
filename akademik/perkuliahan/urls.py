

from django.urls import path,include
from . import views

urlpatterns = [

    path('dashboard/',views.dashboard,name='home'),
    path('profil/',views.profil,name='manage_profil'),
    path('matakuliah/',views.matakuliah,name='manage_matakuliah'),
    path('mahasiswa-baru/',views.mahasiswa,name='manage_mahasiswa'),
    path('jurusan/',views.Jurusan,name='manage_jurusan'),
    path('tambah_Jurusan',views.tambah_Jurusan,name='tambah_Jurusan'),
]

