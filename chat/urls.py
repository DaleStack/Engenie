from django.urls import path
from .views import generate_CreativeWriting, generate_ResearchAssistance

urlpatterns = [
    path('chat/<int:pk>/', generate_CreativeWriting, name='creative_writing'),
    path('chat/<int:pk>/', generate_ResearchAssistance, name='research_assistance'),
]
