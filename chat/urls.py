from django.urls import path
from .views import generate_CreativeWriting, generate_ResearchAssistance, generate_Brainstorm

urlpatterns = [
    path('chat/<int:pk>/', generate_CreativeWriting, name='creative_writing'),
    path('chat/<int:pk>/', generate_ResearchAssistance, name='research_assistance'),
    path('chat/<int:pk>/', generate_Brainstorm, name='brainstorm'),
]
