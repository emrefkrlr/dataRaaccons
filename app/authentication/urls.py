from django.urls import path
from authentication import views

app_name = "authentication" 

urlpatterns = [
    path('login/', views.login, name='login'),
    path('login/<str:confirm>/', views.login, name='login'),
    path('create_account/', views.create_account, name='create_account'),
    path('logout/', views.logout, name='logout'),
    
]