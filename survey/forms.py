from django import forms
from .models import Questionnaire

class QuestionnaireForm(forms.ModelForm):
    class Meta:
        model = Questionnaire
        fields = ['full_name', 'academic_strengths', 'grade', 'aspirations', 'learning_preferences']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Full Name'}),
            'academic_strengths': forms.Select(choices=[
                ('Somali', 'Somali'), ('English', 'English'), ('Arabic', 'Arabic'),
                ('Tarbiyya (Education)', 'Tarbiyya (Education)'), ('Math', 'Math'),
                ('Physics', 'Physics'), ('Biology', 'Biology'), ('Chemistry', 'Chemistry'),
                ('Technology', 'Technology'), ('History', 'History'), ('Geography', 'Geography')
            ]),
            'grade': forms.Select(choices=[
                ('A+', 'A+'), ('A', 'A'), ('A-', 'A-'), ('B+', 'B+'), ('B', 'B'),
                ('B-', 'B-'), ('C+', 'C+'), ('C', 'C'), ('C-', 'C-'), ('D', 'D'), ('F', 'F')
            ]),
            'aspirations': forms.Select(choices=[
                ('Doctor', 'Doctor'), ('Engineer', 'Engineer'), ('Artist', 'Artist'),
                ('Entrepreneur', 'Entrepreneur'), ('Scientist', 'Scientist'), ('Teacher', 'Teacher')
            ]),
            'learning_preferences': forms.Select(choices=[
                ('Visual', 'Visual (learning by seeing)'), ('Auditory', 'Auditory (learning by hearing)'),
                ('Kinesthetic', 'Kinesthetic (learning by doing)'), ('Reading/Writing', 'Reading/Writing')
            ]),
        }
