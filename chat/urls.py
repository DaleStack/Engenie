from django.urls import path
from .views import generate_generic_view

urlpatterns = [
    path("chat/<int:pk>/<str:mode>/", generate_generic_view, name="generate_content")
]
