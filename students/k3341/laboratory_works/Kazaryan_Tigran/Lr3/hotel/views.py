from django.shortcuts import render
from rest_framework import viewsets
from .models import Apartments, Guest, Resident, Cleaner, CleanSchedule, Floor
from rest_framework.decorators import action
from . import serializers
from .utils import get_tokens_for_user
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from django.contrib.auth.models import User
from datetime import datetime as dt
# Create your views here.

"""Auth views"""


class RegistrationView(generics.CreateAPIView):
    serializer_class = serializers.RegistrationSerializer
    queryset = User.objects.all()


class LoginView(generics.GenericAPIView):
    serializer_class = serializers.LoginSerializer
    queryset = User.objects.all()

    def post(self, request):
        if 'username' not in request.data or 'password' not in request.data:
            return Response({'msg': 'Credentials missing'}, status=status.HTTP_400_BAD_REQUEST)
        username = request.data.get("username", None)
        password = request.data.get("password", None)
        print(username, password)
        if username is not None and password is not None:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                auth_data = get_tokens_for_user(request.user)
                return Response({'msg': 'Login Success', **auth_data}, status=status.HTTP_200_OK)
            return Response({'msg': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    serializer_class = serializers.LogoutSerializer
    queryset = User.objects.all()
    def post(self, request):
        logout(request)
        return Response({'msg': 'Successfully Logged out'}, status=status.HTTP_200_OK)


class ChangePasswordView(generics.GenericAPIView):
    serializer_class = serializers.PasswordChangeSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request.user.set_password(serializer.validated_data['new_password'])
        request.user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ApartmentsViewSet(viewsets.ModelViewSet):
    queryset = Apartments.objects.all()
    serializer_class = serializers.ApartmentsSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['GET'])
    def count_free(self, request):
        count = Apartments.objects.filter(status="free").count()
        return Response({"Free": count})



class GuestViewSet(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    permission_classes = [IsAuthenticated]


    def get_serializer_class(self):
        if self.action == "find":
            return serializers.FindGuestSerializer
        return serializers.GuestSerializer

    @action(detail=False, methods=['POST'])
    def find(self, request):
        city = request.data.get("city", None)
        qs = self.queryset.filter(city=city)
        if len(qs):
            return Response({"city": city, "count": len(qs)})
        else:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        
class FloorViewSet(viewsets.ModelViewSet):
    queryset = Floor.objects.all()
    serializer_class = serializers.FloorSerializer
    permission_classes = [IsAuthenticated]

class ResidentViewSet(viewsets.ModelViewSet):
    queryset = Resident.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "find":
            return serializers.FindResidentSerializer
        if self.action == "other_resident":
            return serializers.OtherResidentsSerializer
        if self.action == "get_cleaner":
            return serializers.CleanerForResident
        return serializers.ResidentSerializer

    @action(detail=False, methods=['POST'])
    def find(self, request):
        check_in = request.data.get("check_in", None)
        check_out = request.data.get("check_out", None)
        apartment = request.data.get("apartment_number", None)
        qs = self.queryset.filter(apartment_number=apartment, check_out__gte=check_out, check_in__lte=check_in)
        ser = serializers.ShowResidentSerializer(qs, many=True)

        return Response(ser.data)

    @action(detail=True, methods=['GET'])
    def other_residents(self, request, pk=None):
        obj = self.get_object()
        qs = Resident.objects.filter(check_in__lte=obj.check_out, check_out__gte=obj.check_in).exclude(id=obj.id)
        ser = serializers.OtherResidentsSerializer(qs, many=True)
        return Response(ser.data)

    @action(detail=False, methods=['post'])
    def get_cleaner(self, request):
        serializer = serializers.CleanerForResident(data=request.data)
        if serializer.is_valid():
            resident_name = serializer.validated_data['passport_number']
            day = serializer.validated_data['day']
            try:
                resident = Resident.objects.get(passport_number=resident_name)
                schedule = CleanSchedule.objects.get(floor=resident.apartment_number.floor, day=day)
                cleaner = Cleaner.objects.get(sch_cleaner_id=schedule.id)
                ser = serializers.CleanerSerializer(cleaner)
                return Response(ser.data)
            except Guest.DoesNotExist:
                return Response({'error': 'Guest not found'}, status=status.HTTP_404_NOT_FOUND)
            except CleanSchedule.DoesNotExist:
                return Response({'error': 'Clean schedule not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CleanerViewSet(viewsets.ModelViewSet):
    queryset = Cleaner.objects.all()
    serializer_class = serializers.CleanerSerializer
    permission_classes = [IsAuthenticated]


class CleanScheduleViewSet(viewsets.ModelViewSet):
    queryset = CleanSchedule.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "find":
            return serializers.FindScheduleSerializer
        return serializers.CleanScheduleSerializer




class ReportViewSet(viewsets.ModelViewSet):
    queryset = Apartments.objects.all()
    serializer_class = serializers.ReportSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, quarter):

        if quarter not in ["1","2","3","4"]:
            return Response({"error": "Quarter parameter is incorrect"}, status=status.HTTP_400_BAD_REQUEST)

        def get_quarter_dates(quarter):
            year = 2024
            if quarter == "1":
                start_date = dt(year, 1, 1)
                end_date = dt(year, 3, 31)
            elif quarter == "2":
                start_date = dt(year, 4, 1)
                end_date = dt(year, 6, 30)
            elif quarter == "3":
                start_date = dt(year, 7, 1)
                end_date = dt(year, 9, 30)
            elif quarter == "4":
                start_date = dt(year, 10, 1)
                end_date = dt(year, 12, 31)
            else:
                raise ValueError("Invalid quarter number")
            return start_date, end_date

        start_date, end_date = get_quarter_dates(quarter)
        serializer_context = {
            'start_date': start_date,
            'end_date': end_date
        }
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True, context=serializer_context)
        return Response(serializer.data)