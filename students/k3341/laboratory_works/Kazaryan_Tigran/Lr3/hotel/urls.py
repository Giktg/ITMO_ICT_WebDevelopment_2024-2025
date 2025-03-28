from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.SimpleRouter()

router.register('apartments', viewset=views.ApartmentsViewSet)
router.register('guest', viewset=views.GuestViewSet)
router.register('floor', viewset=views.FloorViewSet)
router.register('resident', viewset=views.ResidentViewSet)
router.register('cleaner', viewset=views.CleanerViewSet)
router.register('schedule', viewset=views.CleanScheduleViewSet)
router.register('report', viewset=views.ReportViewSet, basename='quarterly_report')



urlpatterns = [
    path('report/<str:quarter>/', views.ReportViewSet.as_view({'get': 'list'}), name='report'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('change-password/<int:pk>/', views.ChangePasswordView.as_view(), name='change-password'),
    path('', include(router.urls)),
]