from django.shortcuts import render
from blog.models import Postear
from django.shortcuts import render, get_object_or_404

# Create your views here.
def listar_articulo(request):
    articulo = Postear.objects.all()
    return render (request,'blog/listar_articulo.html',{'articulo':articulo})

def detalle_articulo(request, pk):
    post = get_object_or_404(Postear, pk=pk)
    return render(request, 'blog/detalle_articulo.html', {'post': post})
