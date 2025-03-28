from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Guest(models.Model):
    passport_number = models.CharField(max_length=11, primary_key=True)
    guest_name = models.CharField(max_length=255)
    city = models.CharField(max_length=30)

    def __str__(self):
        return str(self.passport_number)



class Floor(models.Model):
    floor = models.IntegerField(primary_key=True)

    def __str__(self):
        return f"{self.floor}"


class Apartments(models.Model):
    apartment_number = models.CharField(max_length=4, primary_key=True)
    rooms = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)])
    price = models.IntegerField()
    floor = models.ForeignKey(Floor, related_name='apart_number', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=(
        ('free', 'free'),
        ('rented', 'rented'),
        ('booked', 'booked'),
        ('renovation', 'renovation')
    ))
    phone = models.CharField(max_length=12)

    def __str__(self):
        return self.apartment_number

class Resident(models.Model):
    passport_number = models.ForeignKey(Guest, related_name='resident_passport', on_delete=models.CASCADE)
    apartment_number = models.ForeignKey(Apartments, related_name='apart_number', on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f"{self.passport_number} - {self.apartment_number}"


class Cleaner(models.Model):
    cleaner_name = models.CharField(max_length=255, primary_key=True)

    def __str__(self):
        return f"{self.cleaner_name}"
    

class CleanSchedule(models.Model):
    cleaner_id = models.ForeignKey(Cleaner, related_name='sch_cleaner_id', on_delete=models.CASCADE)
    floor = models.ForeignKey(Floor, related_name='sch_floor', on_delete=models.CASCADE)
    day = models.CharField(max_length=10, choices=(
        ('пн', 'пн'),
        ('вт', 'вт'),
        ('ср', 'ср'),
        ('чт', 'чт'),
        ('пт', 'пт'),
        ('сб', 'сб'),
        ('вс', 'вс'),
    ))

    def __str__(self):
        return f"{self.day} на {self.floor} этаже"


