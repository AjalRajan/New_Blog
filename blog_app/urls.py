

from django.urls import path
from blog_app.views import *
urlpatterns = [

    path('', Home.as_view() , name = 'home'),
    path('blog_detail/<int:pk>', Detail.as_view() , name = 'detail'),
    path('add_blog/' , AddBlog.as_view() , name = 'addblog'),

    path('update_blog/<int:pk>' , Update.as_view() , name = 'update'),
    path('delete_blog/<int:pk>' , Delete.as_view() , name = 'delete')
]
