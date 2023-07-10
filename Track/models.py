from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name
    
    def connected_employees(self):
        return ", ".join(self.employees.values_list('user__username', flat=True))

    
    
    
#I am using here build in User in django for Employee
class Employee(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    company = models.ForeignKey(Company,on_delete=models.CASCADE, related_name="employees")
    


class Device(models.Model):
    Company = models.ForeignKey(Company,on_delete=models.CASCADE,related_name="devices")
    name = models.CharField(max_length=100)
    
    
class DeviceAllocation(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name="device_allocation")
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE,related_name="employees")
    start_date = models.DateField()
    end_date = models.DateField()


class DeviceLog(models.Model):
    device_allocation = models.ForeignKey(DeviceAllocation, on_delete=models.CASCADE,related_name="device_allocation")
    condition = models.TextField()
    checkout_date = models.DateTimeField(auto_now_add=True)
    checkin_date = models.DateTimeField(blank=True, null=True)