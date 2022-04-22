from django.contrib import admin
from .models import*

# Register your models here.

admin.site.register(User)

admin.site.register(Location)

admin.site.register(Departments)

admin.site.register(Hospital)

admin.site.register(Hospital_Services)
admin.site.register(Our_Doctors)

admin.site.register(Our_Patients)

admin.site.register(Appointments)

admin.site.register(Medication)
admin.site.register(Disease)

admin.site.register(Bills)

admin.site.register(Emergency)

