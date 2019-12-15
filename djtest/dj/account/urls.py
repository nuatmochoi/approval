from django.urls import path
from dj import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.LoginView, name= 'login'),

]