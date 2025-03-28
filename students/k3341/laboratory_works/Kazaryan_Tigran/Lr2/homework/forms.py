from django import forms
from .models import SubmittedHomework, Homework

class HomeworkAnswerForm(forms.ModelForm):
    class Meta:
        model = SubmittedHomework
        fields = ['answer_text']

class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ['subject', 'description', 'due_date']

class GradeHomeworkForm(forms.ModelForm):
    class Meta:
        model = SubmittedHomework
        fields = ['grade', 'is_accepted']
