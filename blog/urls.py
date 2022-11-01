from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

urlpatterns = [
    
    path('blog/', views.PostList.as_view(), name='posts'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('delete_comment/<int:comment_id>', views.delete_comment,
         name='delete_comment'),
    path('edit_comment/<int:pk>', views.Editcomment.as_view(),
         name='edit_comment'),
    
]