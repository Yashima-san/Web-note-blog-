from django.urls import path, re_path
from hello import views
 
urlpatterns = [
    path('', views.index),
    path("user/<name>", views.user),
    re_path(r"^user/(?P<name>\D+)/(?P<age>\d+)", views.user),
    re_path(r"^user/(?P<name>\D+)", views.user),
    re_path(r"^user", views.user),
    path('about/', views.about, kwargs={"name": "Tom", "age": 38}),  # Добавить слеш здесь
    path('contact/', views.contact),  # Также добавляем слеш для контактов
]
