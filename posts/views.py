from django.shortcuts import render
from django.views.generic import View
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect
from django.utils import timezone


class ListView(View):
	def get(self,request):
		template_name = 'lista.html'
		posts = Post.objects.all().order_by('titulo')
		compa = {
		'posts':posts,
		}
		return render(request,template_name,compa)


class DetailView(View):
	def get(self,request,slug):
		template_name = 'detalle.html'
		post = Post.objects.get(slug=slug)
		context = {
		'post':post
		}
		return render(request,template_name,context)

def post_new(request):#Permite guardar nuevos post en la base de datos que se crea en /post/new#}
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('/blog/', pk=post.pk)#al terminar el post nos envia a la principal#}
	else:
		form = PostForm()
	return render(request, 'posteando.html', {'form': form})