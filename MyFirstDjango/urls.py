from django.contrib import admin
from django.urls import path
from todo_list import views as todo_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todo_views.home, name='home'),
    path('about/', todo_views.about, name='about'),
]
