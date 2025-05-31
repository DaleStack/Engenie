from django.shortcuts import render, redirect, get_object_or_404
from .models import PromptTemplate
import google.generativeai as genai
from django.conf import settings
import markdown
from django.utils.safestring import mark_safe
# Create your views here.

def generate_CreativeWriting(request, pk):
    template = get_object_or_404(PromptTemplate, pk=pk)

    if request.method == "POST":
        idea = request.POST.get("Idea")
        description = request.POST.get("Description")
        tone = request.POST.get("Tone")

        # Format prompt from template with user input
        prompt = template.content.format(Idea=idea, Description=description, Tone=tone)

        # Configure Gemini API
        genai.configure(api_key=settings.GOOGLE_API_KEY)
        model = genai.GenerativeModel("gemini-2.0-flash")

        try:
            # Generate content from model
            result = model.generate_content(prompt)
            if hasattr(result, "text"):
                generated_markdown = result.text
            else:
                generated_markdown = str(result)

            # Convert Markdown to HTML safely
            html_result = mark_safe(markdown.markdown(generated_markdown))

        except Exception as e:
            html_result = f"<p>Error generating content: {e}</p>"

        return render(request, "chat/result.html", {
            "idea": idea,
            "description": description,
            "tone": tone,
            "template": template,
            "prompt": prompt,
            "result": html_result,
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

        # Format prompt from template with user input
        prompt = template.content.format(Idea=idea, Description=description, Tone=tone)

        # Configure Gemini API
        genai.configure(api_key=settings.GOOGLE_API_KEY)
        model = genai.GenerativeModel("gemini-2.0-flash")

        try:
            # Generate content from model
            result = model.generate_content(prompt)
            if hasattr(result, "text"):
                generated_markdown = result.text
            else:
                generated_markdown = str(result)

            # Convert Markdown to HTML safely
            html_result = mark_safe(markdown.markdown(generated_markdown))

        except Exception as e:
            html_result = f"<p>Error generating content: {e}</p>"

        return render(request, "chat/result.html", {
            "idea": idea,
            "description": description,
            "tone": tone,
            "template": template,
            "prompt": prompt,
            "result": html_result,
        })

    return render(request, "chat/ResearchAssistance.html", {
        "template": template
    })
