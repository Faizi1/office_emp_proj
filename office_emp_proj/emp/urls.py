from django.urls import path
from emp import views

urlpatterns = [
    path('index/', views.index, name ="index"),
]
