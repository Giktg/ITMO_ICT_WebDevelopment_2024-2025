from rest_framework import serializers
from .models import Apartments, Guest, Resident, Cleaner, CleanSchedule, Floor
from django.contrib.auth.models import User
from django.db.models import Count, Sum
"""Auth serializers"""


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.pop('password2')
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password Does not match")
        return attrs

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password',]


class LogoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = []


class PasswordChangeSerializer(serializers.ModelSerializer):
    current_password = serializers.CharField(style={"input_type": "password"}, required=True)
    new_password = serializers.CharField(style={"input_type": "password"}, required=True)

    class Meta:
        model = User
        fields = ['current_password', 'new_password']

    def validate_current_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError({'current_password': 'Does not match'})
        return value


"""Main serializers"""


class ApartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartments
        fields = "__all__"


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = "__all__"


class FloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Floor
        fields = "__all__"


class ResidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resident
        fields = "__all__"


class CleanerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cleaner
        fields = "__all__"


class CleanScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CleanSchedule
        fields = "__all__"


class FindGuestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Guest
        fields = ['city']


class FindResidentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resident
        exclude = ['passport_number']


class ShowResidentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resident
        fields = '__all__'


class FindScheduleSerializer(serializers.ModelSerializer):
    resident = serializers.CharField(source='resident.passport_number.guest_name')

    class Meta:
        model = CleanSchedule
        fields = ['day', 'resident']


class OtherResidentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resident
        fields = ['passport_number', 'apartment_number', 'check_in', 'check_out']


class CleanerForResident(serializers.Serializer):

    guest_name = serializers.PrimaryKeyRelatedField(queryset=Guest.objects.all(), source='passport_number', write_only=True)
    day = serializers.ChoiceField(choices=('пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс'))
    class Meta:
        model = Resident
        fields = ['passport_number', 'day']


class ShowCleanerSerializer(serializers.Serializer):

    class Meta:
        model = Cleaner
        fields = ['cleaner_name']

class ReportSerializer(serializers.Serializer):
    apartment_number = serializers.CharField()
    total_clients = serializers.SerializerMethodField()
    total_income = serializers.SerializerMethodField()

    def get_total_clients(self, obj):
        start_date = self.context.get('start_date')
        end_date = self.context.get('end_date')
        print(start_date,end_date)
        return Resident.objects.filter(apartment_number=obj, check_in__gt=start_date, check_out__lte=end_date).count()

    def get_total_income(self, obj):
        start_date = self.context.get('start_date')
        end_date = self.context.get('end_date')
        residents = Resident.objects.filter(apartment_number=obj, check_in__gt=start_date, check_out__lte=end_date)
        price = 0
        days = 0
        for resident in residents:
            price = resident.apartment_number.price
            date = resident.check_out - resident.check_in
            days += date.days
        total_income = price*days
        return total_income

