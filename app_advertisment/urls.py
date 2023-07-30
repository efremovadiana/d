from django.urls import path 
from .views import index, top_sellers, register

urlpatterns = [
    path('', index, name='index'),
    path('top_sellers', top_sellers, name='top_sellers'),
    #path('advertisment_post', advertisment_post, name='advertisment_post'),    
    #path('login', login, name='login'),   
    #path('profile', profile, name='profile'),
    path('register', register, name='register'),
    #path('advertisment', advertisment, name='advertisment'),
]
