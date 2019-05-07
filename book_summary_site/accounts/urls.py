from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('register/',views.regist_user,name='regist'),
]