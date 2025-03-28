from django.contrib import admin

# Register your models here.
from .models import Apartments, Guest, Resident, Cleaner, CleanSchedule, Floor

admin.site.register(Apartments)
admin.site.register(Guest)
admin.site.register(Resident)
admin.site.register(Cleaner)
admin.site.register(CleanSchedule)
admin.site.register(Floor)
