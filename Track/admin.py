from django.contrib import admin
from Track.models import Company,Employee,Device,DeviceAllocation,DeviceLog
# Register your models here.


@admin.register(Company)
class CompanyModel(admin.ModelAdmin):
    list_display=["name",'connected_employees']
    
    
@admin.register(Employee)
class EmployeeModel(admin.ModelAdmin):
    list_display=["user"]
    
    
   

