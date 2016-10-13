from django.shortcuts import render
from blog.models import Postear
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.utils import timezone
from django.shortcuts import redirect


# Create your views here.
def listar_articulo(request):
    articulo = Postear.objects.all()
    return render (request,'blog/listar_articulo.html', {'articulo':articulo})

def detalle_articulo(request, pk):
    post = get_object_or_404(Postear, pk=pk)
    return render(request, 'blog/detalle_articulo.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.fecha_creacion = timezone.now()
            post.save()
            return redirect('blog.views.detalle_articulo', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Postear, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('blog.views.detalle_articulo', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
