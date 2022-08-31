from django.urls import path
from dashboard import views

app_name = "dashboard" 

urlpatterns = [
    path('<str:activity>/', views.dashboard, name='activity'),
    path('<str:activity>/category/<str:activity_category>/', views.dashboard, name='activity_category'),
    
    
    
    
]