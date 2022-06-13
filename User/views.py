from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


class userreg(CreateView):

	form_class = UserCreationForm

	template_name = 'registration/reg.html'

	success_url = reverse_lazy('login')