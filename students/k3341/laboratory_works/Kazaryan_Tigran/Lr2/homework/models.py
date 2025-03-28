from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from django.db import models
from django.utils.timezone import now


class Subject(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'is_staff': True},
        verbose_name="Преподаватель",
        related_name="subjects_taught"
    )
    students = models.ManyToManyField(
        User,
        related_name="subjects_enrolled"
    )

    def __str__(self):
        return self.name


class Homework(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="Предмет")
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_staff': True}, verbose_name="Преподаватель")
    issue_date = models.DateField(default=now, verbose_name="Дата выдачи")
    due_date = models.DateField(verbose_name="Срок выполнения")
    description = models.TextField(verbose_name="Текст задания")
    penalty_info = models.TextField(blank=True, null=True, verbose_name="Информация о штрафах")

    def __str__(self):
        return f"{self.subject} - {self.due_date}"

class SubmittedHomework(models.Model):
    homework = models.ForeignKey('Homework', on_delete=models.CASCADE, verbose_name="Задание")
    student = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Ученик", limit_choices_to={'is_staff': False})
    answer_text = models.TextField(verbose_name="Ответ")
    grade = models.IntegerField(blank=True, null=True, verbose_name="Оценка")
    submit_date = models.DateTimeField(default=timezone.now, verbose_name="Дата сдачи")
    is_accepted = models.BooleanField(default=False)

    class Meta:
        unique_together = ('student', 'homework')

    def __str__(self):
        return f"{self.student} - {self.homework}"