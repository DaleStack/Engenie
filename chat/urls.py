from django.urls import path
from .views import generate_generic_view, home_view

urlpatterns = [
    path("chat/<int:pk>/<str:mode>/", generate_generic_view, name="generate_content"),
    path('', home_view, name="home_view"),
]
