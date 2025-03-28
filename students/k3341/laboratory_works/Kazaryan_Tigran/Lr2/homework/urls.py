from django.urls import path
from .views import homework_list, submit_homework, homework_detail, assigned_homework, create_homework, \
    student_homework, delete_homework, homework_submission_review

urlpatterns = [
    path('list/', homework_list, name='homework_list'),
    path('homework/<int:id>/', homework_detail, name='homework_detail'),
    path('assigned_homework/', assigned_homework, name='assigned_homework'),
    path('create_homework/', create_homework, name='create_homework'),
    path('delete/<int:homework_id>/', delete_homework, name='delete_homework'),
    path('student/homework/', student_homework, name='student_homework'),
    path('homework/<int:homework_id>/submit/', submit_homework, name='submit_homework'),
    path('homework/submission/<int:submission_id>/', homework_submission_review, name='homework_submission_review'),


]
