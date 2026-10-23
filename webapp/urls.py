from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.my_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.my_logout, name='logout'),
 
    path('createrecord/', views.create_record, name='createrecord'),
    path('viewrecord/<int:record_id>/', views.view_record, name='viewrecord'),
    path('updaterecord/<int:record_id>/', views.update_record, name='updaterecord'),
    path('deleterecord/<int:record_id>/', views.delete_record, name='deleterecord'),
    path('search-records/', views.search_records, name='search-records'),
    
]
