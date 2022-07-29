from django.urls import path
from authentication import views

app_name = "authentication" 

urlpatterns = [
    path('login/', views.login, name='login'),
    path('login/<str:confirm>/', views.login, name='login'),
    path('create_account/', views.create_account, name='create_account'),
    path('create_account/<str:package>/', views.create_account, name='create_account'),
    path('logout/', views.logout, name='logout'),
    path("password_reset/", views.reset_password, name="password_reset"),
    path("new_password/<str:token>/", views.set_new_password, name="set_new_password"),

    
]