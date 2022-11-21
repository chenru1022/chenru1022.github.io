from week10project import views
from django.urls import path

urlpatterns = [
    path("", views.home),
    path("ccu411422059", views.ccu411422059_function)
]
