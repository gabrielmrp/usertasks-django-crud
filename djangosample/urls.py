from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .router import router
from usertasksapi import views
from django.shortcuts import render


urlpatterns = [
    path('',views.user, name='user_home'), 
    path('api/',include(router.urls)),
    path('user/',views.user, name='user'),   
    path('usertasks/<int:user_id>/',views.usertasks, name='usertask'),
    
    path('api/user/',views.api_users, name='api_users'), 
    path('api/user/<int:id>',views.api_user, name='api_user'),

       
    path('api/usertasks/<int:userid>',views.api_user_tasks, name='api_user_tasks'),  
    path('api/task/<int:id>',views.api_task, name='api_task'), 
     
     
]
urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 