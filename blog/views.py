from django.shortcuts import render,get_object_or_404
# from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView
from blog.models import Post
# from blog.serializers import PostSerializer,PostDetailSerializer,PostCreateSerializer
# from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.settings import api_settings
from django.views.generic import ListView,TemplateView,DetailView
from blog.forms import PostForm
from django.views.generic.edit import FormView,UpdateView,DeleteView
# Create your views here.

    #Normal generic views

class HomeView(TemplateView):
	model = Post
	template_name = 'base.html'

class postdetailview(DetailView):
	queryset = Post.objects.all()
	template_name = 'detail.html'

	def get_context(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Post,id=id_)

class postview(ListView):
	queryset = Post.objects.all()
	template_name = 'content.html'

class postcreate(FormView):
	template_name = 'form.html'
	form_class = PostForm
	success_url = '/posts/'

	def form_valid(self, form):
		form.save()
		return super().form_valid(form)


class postupdate(UpdateView):
	template_name = 'form.html'
	form_class = PostForm
	success_url = '/posts/'
	queryset = Post.objects.all()


	def get_context(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Post,id=id_)

	def form_valid(self, form):
		form.save()
		return super().form_valid(form)


class postdeleteview(DeleteView):
	queryset = Post.objects.all()
	template_name = 'delete.html'
	success_url = '/posts/'

	def get_context(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Post,id=id_)









	#Api views

# class PostView(ListAPIView):
# 	queryset = Post.objects.all()
# 	serializer_class = PostSerializer

# class PostDetailView(RetrieveAPIView):
# 	queryset = Post.objects.all()
# 	serializer_class = PostDetailSerializer


# class PostCreateView(CreateAPIView):
# 	queryset = Post.objects.all()
# 	serializer_class = PostCreateSerializer

# class UserLoginView(ObtainAuthToken):
# 	"""Handle creating user authentication token"""
# 	renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES