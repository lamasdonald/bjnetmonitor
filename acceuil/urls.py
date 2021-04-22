from django.urls import include, path
from . import views


urlpatterns = [
    path("", views.acceuil, name="Acceuil"),
]