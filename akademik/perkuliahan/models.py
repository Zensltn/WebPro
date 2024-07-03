from django.db import models

# Create your models here.
class jurusan(models.Model):
    kodejurusan= models.CharField(max_length=50,null=False,blank=False,verbose_name='Kode Prodi')
    namajurusan= models.CharField(max_length=150,null=False,blank=False,verbose_name='Program studi')
    level =(
        ('S1','STRATA 1'),
        ('S2','STRATA 2'),
        ('S3','STRATA 3'),
        ('D3','DIPLOMA 3'),
         ('D4','DIPLOMA 4'),
    )
    jenjang= models.CharField (max_length=150,null=True,blank=True,verbose_name='jenjang',choices=level)

    def __str__(self):
        return self.namajurusan 

class Mahasiswa(models.Model):
    nim = models.CharField(max_length=50,null=False,blank=False,verbose_name='Nim')
    namalengkap = models.CharField(max_length=150,null=False,blank=False,verbose_name='Nama Lengkap')
    jeniskelamin = (
        ('L','LAKI-LAKI'),
        ('P','PEREMPUAN'),
    )
    jk = models.CharField(max_length=50,verbose_name='Jenis Kelamin',choices=jeniskelamin)
    email = models.EmailField(null=True,verbose_name='E-Mail')
    jurusan = models.ForeignKey(jurusan,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.namamahasiswa
    

class matakuliah(models.Model):
    kodemk = models.CharField(max_length=100,null=False,blank=False,verbose_name='Kode Matakuliah')
    namamk = models.CharField(max_length=150,null=False,blank=False,verbose_name='Nama Matakuliah')
    semester = models.CharField(max_length=50,verbose_name='Semester')
    Sks = models.IntegerField(verbose_name='SKS')
    jurusan = models.ForeignKey(jurusan,on_delete=models.CASCADE)
        
    def __str__(self):
        return self.namamk

class Dosen(models.Model):
    nidn = models.CharField(max_length=20, verbose_name='Nidn',null=False,blank=False)
    namadosen =models.CharField(max_length=150,verbose_name='NamaLengkap')
    gelar = models.CharField(max_length=30,verbose_name='Gelar',help_text='S.Kom. ,M.Kom')
    tgllahir =models.DateField(verbose_name='Tanggal Lahir', null=True,blank=True)
    templahir =models.CharField(max_length=100, verbose_name='Tempat Lahir',null=True,blank=True)
    jurusan =models.ForeignKey(jurusan,on_delete=models.CASCADE,default=" ",verbose_name='Program Studi')
    foto = models.ImageField(verbose_name='Foto',null=False,blank=False,upload_to='foto mhs')
    cv = models.FileField(verbose_name='CV',null=False,blank=False,upload_to='cv_dosen')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nidn
    