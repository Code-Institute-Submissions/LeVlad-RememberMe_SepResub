from django.contrib import admin
from django.urls import path, include
from tasks import views


urlpatterns = [
    path('', views.get_reminder_list, name='reminder_list'),
    path('', views.home, name='home'),
    path('add', views.add_task, name='add'),
    path('edit/<task_id>', views.edit_task, name='edit'),
    path('toggle/<task_id>', views.toggle_task, name='toggle'),
    path('delete/<task_id>', views.delete_task, name='delete'),
]