

from django.urls import path,include
from . import views

urlpatterns = [

    path('dashboard/',views.dashboard,name='home'),
    path('profil/',views.profil,name='manage_profil'),
    path('matakuliah/',views.matakuliah,name='manage_matakuliah'),
    path('mahasiswa-baru/',views.mahasiswa,name='manage_mahasiswa'),
    path('jurusan/',views.Jurusan,name='manage_jurusan'),   
    path('tambah_Jurusan',views.tambah_jurusan,name='tambah_Jurusan'),
    path('edit-jurusan/<int:jurusanid>/',views.edit_jurusan,name='edit_jurusan'),
    path('hapus-jurusan/<int:jurusanid>/',views.hapus_jurusan,name='hapus_jurusan'),
    path('mahasiswa/',views.mahasiswa,name='manage_mahasiswa'),
    path('tambah-mahasiswa/',views.tambah_mahasiswa,name='tambah_mahasiswa'),
    path('edit-mahasiswa/<int:mhsid>/',views.edit_mahasiswa,name='edit_mahasiswa'),
    path('hapus-mahasiswa/<int:mhsid>/',views.hapus_mahasiswa,name='hapus_mahasiswa'),
    path('dosen/',views.dosen, name='manage_dosen'),
    path('tambah-dosen/',views.tambah_dosen, name='tambah_dosen'),
    path('View-dosen/<int:dosenid>',views.viewdosen, name='view_dosen'),
    
]

