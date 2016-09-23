from django.shortcuts import render

# Create your views here.
def listar_articulo(request):
    return render (request,'blog/listar_articulo.html',{})
