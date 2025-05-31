from django.shortcuts import render, redirect, get_object_or_404
from .models import PromptTemplate
import google.generativeai as genai
from django.conf import settings
# Create your views here.

def generate_CreativeWriting(request, pk):
    template = get_object_or_404(PromptTemplate, pk=pk)

    if request.method == "POST":
        idea = request.POST.get("Idea")
        description = request.POST.get("Description")
        tone = request.POST.get("Tone")

        # Fill the prompt using user input
        prompt = template.content.format(Idea=idea, Description=description, Tone=tone)

        # Configure and call Gemini API
        genai.configure(api_key=settings.GOOGLE_API_KEY)
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(prompt)

        return render(request, "chat/result.html", {
            'idea':idea,
            'description':description,
            'tone':tone,
            "result": response.text,
            "template": template,
            "prompt": prompt,
        })

    return render(request, "chat/CreativeWriting.html", {
        "template": template
    })


def generate_ResearchAssistance(request, pk):
    template = get_object_or_404(PromptTemplate, pk=pk)

    if request.method == "POST":
        idea = request.POST.get("Idea")
        description = request.POST.get("Description")
        tone = request.POST.get("Tone")

        # Fill the prompt using user input
        prompt = template.content.format(Idea=idea, Description=description, Tone=tone)

        # Configure and call Gemini API
        genai.configure(api_key=settings.GOOGLE_API_KEY)
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(prompt)

        return render(request, "chat/result.html", {
            'idea':idea,
            'description':description,
            'tone':tone,
            "result": response.text,
            "template": template,
            "prompt": prompt,
        })

    return render(request, "chat/ResearchAssistance.html", {
        "template": template
    })
