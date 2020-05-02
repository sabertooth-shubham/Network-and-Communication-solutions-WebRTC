from django.contrib import admin
from django.urls import path,include
from . import views
app_name = 'video'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('chatbot',views.chatbot,name='chatbot'),
   

]
