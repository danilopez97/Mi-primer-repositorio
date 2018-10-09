from django.shortcuts import render
from .models import publicacion
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

def listado(request):
        posts=publicacion.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
        return render(request, 'blog/listar.html', {'posts':posts})
# Create your views here.
