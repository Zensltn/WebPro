from django import forms
from .models import jurusan, Mahasiswa , Dosen
from django.forms import NumberInput

class Tambah_jurusan(forms.ModelForm):
    class Meta:
        model = jurusan #tmodel -> tabel tabel jurusan 
        fields ='__all__' #menggunakan semua field yang ada pada tabel jurusan
        
    def clean_kodejurusan(self):
        clean_data = super().clean()
        kodejur = clean_data.get('kodejurusan')
        
        if jurusan.objects.filter(kodejurusan = kodejur).first():
            raise forms.ValidationError("kode jurusan sudah ada")
        return kodejur

    def clean_namajurusan(self):
        clean_data = super().clean()
        namajur = clean_data.get('namajurusan')
        
        if jurusan.objects.filter(namajurusan = namajur).first():
            raise forms.ValidationError("nama jurusan sudah ada")
        return namajur
        
        
class Edit_jurusan(forms.ModelForm):
    class Meta:
        model = jurusan #tmodel -> tabel tabel jurusan 
        fields ='__all__' #menggunakan semua field yang ada pada tabel jurusan
        
class Tambah_mahasiswa(forms.ModelForm):
    class Meta:
        model = Mahasiswa
        fields ='__all__'
        

    def clean_nim(self):
        clean_data = super().clean()
        nimMhs = clean_data.get('nim')
        
        if Mahasiswa.objects.filter(nim = nimMhs).first():
            raise forms.ValidationError("Nim Sudah Ada")
        return nimMhs

    def clean_email(self):
        clean_data = super().clean()
        EmailMhs = clean_data.get('email')
        
        if Mahasiswa.objects.filter(email = EmailMhs).first():
            raise forms.ValidationError("Email Sudah Ada")
        return EmailMhs


class Edit_mahasiswa(forms.ModelForm):
    class Meta:
        model = Mahasiswa
        fields ='__all__' 

class TambahDosen(forms.ModelForm):
    class Meta:
        model= Dosen
        fields ='__all__'
    
    tgllahir=forms.DateField(label='Tanggal Ujikom',widget=NumberInput(attrs={'type':'date'}))