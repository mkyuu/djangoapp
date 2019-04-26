from django.urls import path
from . import views


urlpatterns = [
    path('',views.post_list,name='post_list'),
    path('books/',views.book_list,name='book_list'),
    path('books/<int:pk>/',views.book_detail,name='book_detail')
]