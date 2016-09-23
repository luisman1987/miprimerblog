from django.shortcuts import render
from blog.models import Postear

# Create your views here.
def listar_articulo(request):
    articulo = Postear.objects.all()
    return render (request,'blog/listar_articulo.html',{'articulo':articulo})
