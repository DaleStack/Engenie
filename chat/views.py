from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from .models import PromptTemplate
import google.generativeai as genai
from django.conf import settings
import markdown
from django.utils.safestring import mark_safe
# Create your views here.

# Hardcoded pk-to-mode mapping
TEMPLATE_MODE_MAP = {
    1: "creative-writing",
    2: "research-assistance",
    3: "brainstorm",
}

FORM_TEMPLATES = {
    "creative-writing": ("chat/pages/CreativeWriting.html", "Creative Writing"),
    "research-assistance": ("chat/pages/ResearchAssistance.html", "Research Assistance"),
    "brainstorm": ("chat/pages/Brainstorm.html", "Brainstorm"),
}


def generate_generic_view(request, pk, mode):
    # Validate that the pk exists
    template = get_object_or_404(PromptTemplate, pk=pk)

    # Check if the mode matches what we expect for this pk
    expected_mode = TEMPLATE_MODE_MAP.get(pk)
    if expected_mode != mode:
        return HttpResponseNotFound("Invalid mode for this template ID.")

    # Get the right form/template
    form_template_info = FORM_TEMPLATES.get(mode)
    if not form_template_info:
        return HttpResponseNotFound("Unknown mode.")

    form_template, context_name = form_template_info
    return generate_content_view(request, pk, form_template, context_name)


def generate_content_view(request, pk, form_template, context_name):
    template = get_object_or_404(PromptTemplate, pk=pk)

    if request.method == "POST":
        idea = request.POST.get("Idea")
        description = request.POST.get("Description")
        tone = request.POST.get("Tone")

        prompt = template.content.format(Idea=idea, Description=description, Tone=tone)

        genai.configure(api_key=settings.GOOGLE_API_KEY)
        model = genai.GenerativeModel("gemini-2.0-flash")

        try:
            result = model.generate_content(prompt)
            generated_markdown = getattr(result, "text", str(result))
            html_result = mark_safe(markdown.markdown(generated_markdown))
        except Exception as e:
            html_result = f"<p>Error generating content: {e}</p>"

        return render(request, "chat/pages/result.html", {
            "idea": idea,
            "description": description,
            "tone": tone,
            "template": template,
            "prompt": prompt,
            "result": html_result,
            "context_name": context_name,
        })

    return render(request, form_template, {
        "template": template
    })


