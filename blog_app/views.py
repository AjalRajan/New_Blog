from django.shortcuts import render
from django.views.generic import ListView ,DetailView,CreateView,UpdateView
from blog_app.models import Blog
from .forms import Add_blog



class Home(ListView):

	model = Blog

	template_name = 'Blog/home.html'


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