from django.db import models

class Questionnaire(models.Model):
    full_name = models.CharField(max_length=100)
    academic_strengths = models.CharField(max_length=50)
    grade = models.CharField(max_length=5)
    aspirations = models.CharField(max_length=50)
    learning_preferences = models.CharField(max_length=50)
