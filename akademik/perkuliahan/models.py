from django.db import models

# Create your models here.
class jurusan(models.Model):
    kodejurusan = models.CharField(max_length=50,null=False,blank=False,verbose_name='Kode Prodi')
    namajurusan = models.CharField(max_length=150,null=False,blank=False,verbose_name='Program studi')
    jenjang = models.CharField (max_length=150,null=True,blank=True,verbose_name='jenjang')

def __str__(self):
    return self.namajurusan 


class mahasiswa(models.Model):
    nim = models.CharField(max_length=50,null=False,blank=False,verbose_name='Nim')
    nama = models.CharField(max_length=150,null=False,blank=False,verbose_name='Nama Lengkap')
    jeniskelamin = (
        ('L','LAKI-LAKI'),
        ('P','PEREMPUAN'),
    )
    jk = models.CharField(max_length=50,verbose_name='Jenis Kelamin',choices=jeniskelamin)
    email = models.EmailField(null=True,verbose_name='E-Mail')
    jurusan = models.ForeignKey(jurusan,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nama
    
    class matakuliah(models.Model):
        kodemk = models.CharField(max_length=100,null=False,blank=False,verbose_name='Kode Matakuliah')
        manamk = models.CharField(max_length=150,null=False,blank=False,verbose_name='Nama Matakuliah')
        semester = models.CharField(max_length=50,verbose_name='Semester')
        Sks = models.IntegerField(verbose_name='SKS')
        jurusan = models.ForeignKey(jurusan,on_delete=models.CASCADE)
        
    def __str__(self):
        return self.namamk
        
