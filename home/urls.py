from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),                     # Home
    # path('tasks/', views.task_list, name='task_list'),        # Show tasks

    # path('add/', views.add, name='add'),                      # Page to show add form
    # path('add/save/', views.add_task, name='add_task'),       # Actual saving

    # path('register/', views.regist, name='register'),         # Register

    # path('update/<int:task_id>/', views.update_task, name='update_task'),
    # path('delete/<int:task_id>/', views.delete_task, name='delete_task'),

    # path("save_order/", views.save_order, name="save_order"),

    path('', views.task_list, name='task_list'),
    path('add/', views.add_task, name='add_task'),
    path('update/<int:task_id>/', views.update_task, name='update_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path("save_order/", views.save_order, name="save_order"),
]
