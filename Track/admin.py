from django.contrib import admin
from Track.models import Company,Employee,Device,DeviceAllocation,DeviceLog
# Register your models here.


@admin.register(Company)
class CompanyModel(admin.ModelAdmin):
    list_display=["name",'connected_employees']
    
    
@admin.register(Employee)
class EmployeeModel(admin.ModelAdmin):
    list_display=["user"]
    
@admin.register(Device)
class DeviceModel(admin.ModelAdmin):
    list_display=["name","model","MAC_Address","company"]
    
@admin.register(DeviceAllocation)
class deviceAllocationModel(admin.ModelAdmin):
      list_display=["device","employee","start_date","end_date"]  
