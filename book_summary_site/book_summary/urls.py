from django.urls import path
from . import views

app_name = 'book_summary'

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('book/',views.BookListView.as_view(),name='book_list'),
    path('book/add/',views.BookAddView.as_view(),name='book_add'),
    path('book/<int:pk>/update/',views.BookUpdateView.as_view(),name='book_update'),
    path('book/<int:pk>/',views.BookDetailView.as_view(),name='book_detail'),
    path('book/<int:pk>/delete/',views.BookDeleteView.as_view(),name='book_delete'),
    path('book/<int:book_pk>/comment/',views.CommentView.as_view(),name='comment'),
    path('comment/<int:pk>/delete/',views.CommentDeleteView.as_view(),name='comment_delete'),

]