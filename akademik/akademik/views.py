
from django.http import HttpResponse

def dashboard(request):
    return HttpResponse('<h1> selamat datang di project django </h1>')


def kontak(request):
    return HttpResponse('<h1> ini adalah halaman kontak </h1>')
