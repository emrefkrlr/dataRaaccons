from django.urls import path
from dashboard import views

app_name = "dashboard" 

urlpatterns = [
    path('<str:activity>/', views.activity_overview_dashboard, name='activity'),
    path('<str:activity>/category/<str:activity_category>/', views.activity_category_dashboard, name='activity_category'),
    
    
    
    
]