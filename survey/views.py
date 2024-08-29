import google.generativeai as genai
from django.shortcuts import render, redirect
from .forms import QuestionnaireForm
from .models import Questionnaire

genai.configure(api_key="AIzaSyAz3zwYcagTVnPyJvIlexivk1z1K84G6oc")

model = genai.GenerativeModel(
    model_name="gemini-1.0-pro",
    generation_config={
        "temperature": 0.9,
        "top_p": 1,
        "max_output_tokens": 2048,
        "response_mime_type": "text/plain",
    }
)

def query_gemini(prompt):
    chat_session = model.start_chat(
        history=[{"role": "user", "parts": [prompt]}]
    )
    response = chat_session.send_message(prompt)
    return response.text

def limit_to_100_words(text):
    words = text.split()
    if len(words) > 100:
        return ' '.join(words[:100]) + '...'
    return text

def index(request):
    if request.method == 'POST':
        form = QuestionnaireForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recommendation')
    else:
        form = QuestionnaireForm()
    return render(request, 'index.html', {'form': form})

def recommendation(request):
    last_entry = Questionnaire.objects.last()

    if not last_entry:
        return render(request, 'error.html', {'error': 'No data available'})

    full_name = last_entry.full_name
    strength = last_entry.academic_strengths
    grade = last_entry.grade
    aspiration = last_entry.aspirations
    learning_preference = last_entry.learning_preferences

    prompt = (
        f"Student Name: {full_name}\n"
        f"Academic Strengths: {strength}\n"
        f"Grade: {grade}\n"
        f"Aspirations: {aspiration}\n"
        f"Learning Preferences: {learning_preference}\n"
        "Based on the above information, what major or career would you recommend? Please provide a concise recommendation, limited to 100 words."
    )

    response_text = query_gemini(prompt)

    recommendation = limit_to_100_words(response_text.strip()) if response_text else "No recommendation available."

    context = {
        'full_name': full_name,
        'recommendation': recommendation,
    }

    return render(request, 'recommendation.html', context)
