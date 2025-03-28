from django.contrib import admin
from django.utils import timezone

from .models import Subject, Homework, SubmittedHomework

class SubmittedHomeworkAdmin(admin.ModelAdmin):
    list_display = ('homework', 'student', 'grade', 'answer_text', 'submit_date')
    list_filter = ('homework', 'student')
    search_fields = ('student__username', 'homework__subject__name')
    fields = ('homework', 'student', 'answer_text', 'grade', 'submit_date')
    readonly_fields = ('homework', 'student', 'submit_date')

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.submit_date = timezone.now()
        super().save_model(request, obj, form, change)

admin.site.register(Subject)
admin.site.register(Homework)
admin.site.register(SubmittedHomework, SubmittedHomeworkAdmin)
