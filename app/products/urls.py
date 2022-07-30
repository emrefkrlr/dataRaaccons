from django.urls import path
from products import views

app_name = "products" 

urlpatterns = [
    path('<str:activity>/', views.activity_categorry_list, name='activity_lists'),
    path('category/<str:activity_category>/', views.product_lists, name='product_lists'),
    path('detail/<int:id>/', views.product_deatil, name='product_deatil'),
    #path('<str:activity>/<str:activity_category>/', views.dashboard, name='activity_category'),
    
]