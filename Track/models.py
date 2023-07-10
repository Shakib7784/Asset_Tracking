from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import datetime


class Company(models.Model):
    name = models.CharField(max_length=100, unique=True) 
    def __str__(self):
        return self.name
    #showing username who are belongs to a particular company
    def connected_employees(self):
        return ", ".join(self.employees.values_list('user__username', flat=True))

    
    
    
#I am using here built in User in django for Employee
class Employee(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    company = models.ForeignKey(Company,on_delete=models.CASCADE, related_name="employees")
    
    def __str__(self):
        return self.user.username
    


class Device(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE,related_name="devices",related_query_name="device" )
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=50,default="")
    MAC_Address = models.CharField(max_length=50, unique=True,null=False,default=0) #we can uniquely identify a device by Mac adress
    def __str__(self):
        return self.name
    
    
class DeviceAllocation(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name="device_allocation_device")
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE,related_name="device_allocation_employee")
    start_date = models.DateField()
    end_date = models.DateField()
    def clean(self):
    #check that device and employee are belongs to the same company or not.
        if self.device.company != self.employee.company:
            raise ValidationError("Device and employee must belong to the same company.")
    #check that the device is allocated to the employee previously
        if DeviceAllocation.objects.filter(device=self.device, employee=self.employee).exists():
            raise ValidationError("This device is already allocated to the employee.")


class DeviceLog(models.Model):
    device_allocation = models.ForeignKey(DeviceAllocation, on_delete=models.CASCADE,related_name="device_log")
    checkout_date = models.DateTimeField(auto_now_add=True)
    checkin_date = models.DateTimeField(blank=True, null=True)
    