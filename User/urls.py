

from django.urls import path
from User.views import *

urlpatterns = [

    path('register/', userreg.as_view() , name = 'register')
]
