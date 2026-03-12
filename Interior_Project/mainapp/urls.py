from django.urls import path
from . import views


urlpatterns = [

    # Home page
    path('', views.home, name='home'),

    # Authentication
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # Room selection
    path('rooms/', views.room_select, name='rooms'),

    # Room design form
    path('design/', views.room_design, name='design'),

    # Design result page
    path('result/<int:design_id>/', views.design_result, name='design_result'),

    # Chat page
    path('chat/', views.chat, name='chat'),

    path('my-designs/', views.my_designs, name='my_designs'),

]