from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
class Blog(models.Model):


	title = models.CharField(max_length=20)

	content = models.CharField(max_length=200)

	pub_date = models.DateTimeField(auto_now_add=True)

	author = models.ForeignKey(User, on_delete = models.CASCADE)


	def __str__(self):

		return self.title + ' ' + str(self.author)


	def get_absolute_url(self):

		return reverse('home' , args =(str(self.id)) )

	def get_absolute_url(self):

		return reverse('home' )