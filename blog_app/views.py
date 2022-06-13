from django.shortcuts import render
from django.views.generic import ListView ,DetailView,CreateView,UpdateView,DeleteView
from blog_app.models import Blog
from .forms import Add_blog
from django.urls import reverse_lazy


class Home(ListView):

	model = Blog

	template_name = 'Blog/home.html'

	ordering = ['-pub_date']


class Detail(DetailView):

	model = Blog

	template_name = 'Blog/blog_detail.html'


class AddBlog(CreateView):

	model =Blog

	form_class = Add_blog

	template_name = 'Blog/post_blog.html'

class Update(UpdateView):

	model = Blog


	template_name = 'Blog/Update_blog.html'

	fields = ['title' , 'content']


class Delete(DeleteView):

	model = Blog
	template_name = 'Blog/Delete_blog.html'

	success_url = reverse_lazy('home')