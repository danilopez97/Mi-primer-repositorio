from .models import publicacion
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

def listado(request):
        posts=publicacion.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
        return render(request, 'blog/listar.html', {'posts':posts})
# Create your views here.

def detalle(request, pk):
        post = get_object_or_404(publicacion, pk=pk)
        return render(request, 'blog/detalle.html', {'post': post})

def post_new(request):
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.autor = request.user
                post.save()
                return redirect('detalle', pk=post.pk)
        else:
            form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(publicacion, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('detalle', pk=post.pk)
    else:
        form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})

def post_draft_list(request):
    posts = publicacion.objects.filter(fecha_publicacion__isnull=True).order_by('fecha_creacion')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

def post_publish(request, pk):
    post = get_object_or_404(publicacion, pk=pk)
    post.publish()
    return redirect('detalle', pk=pk)
