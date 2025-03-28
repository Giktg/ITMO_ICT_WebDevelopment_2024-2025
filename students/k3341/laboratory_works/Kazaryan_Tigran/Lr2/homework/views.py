from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Homework, SubmittedHomework
from .forms import HomeworkForm, GradeHomeworkForm, HomeworkAnswerForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

@login_required
def delete_homework(request, homework_id):
    homework = get_object_or_404(Homework, id=homework_id)

    if request.user != homework.teacher:
        return redirect('assigned_homework')

    if request.method == 'POST':
        homework.delete()
        return redirect('assigned_homework')

    return render(request, 'homework/delete_homework.html', {'homework': homework})

@login_required
def create_homework(request):
    if not request.user.is_staff:
        return redirect('home')

    if request.method == 'POST':
        form = HomeworkForm(request.POST)
        if form.is_valid():
            homework = form.save(commit=False)
            homework.teacher = request.user  # Связываем домашку с преподавателем
            homework.save()
            return redirect('assigned_homework')

    else:
        form = HomeworkForm()

    return render(request, 'homework/create_homework.html', {'form': form})

@login_required
def assigned_homework(request):
    if not request.user.groups.filter(name="Преподаватели").exists():
        return redirect('home')

    homeworks = Homework.objects.filter(teacher=request.user)
    print(f"Заданные домашки: {homeworks}")

    return render(request, 'homework/assigned_homework.html', {'homeworks': homeworks})

@login_required
def student_homework(request):
    homeworks = Homework.objects.filter(subject__students=request.user)
    return render(request, 'homework/student_homework.html', {'homeworks': homeworks})


def home(request):
    return render(request, 'account/home.html')

@login_required
def profile(request):
    if request.user.groups.filter(name="Преподаватели").exists():
        assigned_homework = Homework.objects.filter(teacher=request.user)
        student_homework = None
    else:
        assigned_homework = None
        # Показываем все домашние задания, доступные ученику
        student_homework = Homework.objects.filter(subject__students=request.user)

    submitted_homeworks = SubmittedHomework.objects.select_related('homework__subject', 'student').all()

    return render(request, 'account/profile.html', {
        'assigned_homework': assigned_homework,
        'student_homework': student_homework,
        'submitted_homeworks': submitted_homeworks
    })



def homework_detail(request, id):
    homework = get_object_or_404(Homework, id=id)
    return render(request, 'homework/homework_detail.html', {'homework': homework})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def homework_list(request):
    homeworks = Homework.objects.all().order_by('-due_date')  # Сортируем по сроку выполнения (самые поздние вверху)
    return render(request, 'homework/homework_list.html', {'homeworks': homeworks})


@login_required
def submit_homework(request, homework_id):
    homework = get_object_or_404(Homework, id=homework_id)

    if request.user not in homework.subject.students.all():
        return redirect('homework_list')

    if request.method == 'POST':
        form = HomeworkAnswerForm(request.POST)
        if form.is_valid():
            # Сохраняем ответ, но без оценки
            submitted_homework = form.save(commit=False)
            submitted_homework.homework = homework
            submitted_homework.student = request.user
            submitted_homework.save()
            return redirect('student_homework')
    else:
        form = HomeworkAnswerForm()

    return render(request, 'homework/submit_homework.html', {'homework': homework, 'form': form})


@login_required
def grade_homework(request, homework_id, submitted_homework=None):
    homework = get_object_or_404(Homework, id=homework_id)
    if homework.teacher != request.user:
        return redirect('assigned_homework')

    submitted_homeworks = SubmittedHomework.objects.filter(homework=homework)

    if request.method == 'POST':
        form = GradeHomeworkForm(request.POST, instance=submitted_homework)
        if form.is_valid():
            submitted_homework = form.save(commit=False)
            submitted_homework.save()
            return redirect('grade_homework', homework_id=homework.id)
    else:
        form = GradeHomeworkForm()

    return render(request, 'homework/grade_homework.html', {
        'homework': homework,
        'submitted_homeworks': submitted_homeworks,
        'form': form
    })


def homework_submission_review(request, submission_id):
    submission = get_object_or_404(SubmittedHomework, id=submission_id)

    return render(request, 'homework/assigned_homework.html', {'submission': submission})
