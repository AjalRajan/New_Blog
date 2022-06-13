from django import forms
from .models import Blog


class Add_blog(forms.ModelForm):

	class Meta:

		model = Blog

		fields = ('title' , 'content' , 'author' , )

		widgets = {

			'title' :forms.TextInput(attrs = {'class': 'form-control' , 'placeholder' : 'Enter the title'}),

			'content' :forms.Textarea(attrs = {'class': 'form-control' ,'placeholder' : 'Enter the content'}),

			'author' :forms.Select(attrs = {'class': 'form-control'}),
		}