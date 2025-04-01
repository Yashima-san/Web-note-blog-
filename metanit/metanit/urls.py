from django.urls import path, re_path
from hello import views
 
urlpatterns = [
    path('', views.index),
    path("user", views.user),
    path("user/<name>", views.user),
    path("user/<name>/<int:age>", views.user),
    path('about/', views.about, kwargs={"name": "Tom", "age": 38}),  # Добавить слеш здесь
    path('contact/', views.contact),  # Также добавляем слеш для контактов
]
