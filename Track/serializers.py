from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Employee, Company,Device,DeviceAllocation,DeviceLog

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

class DeviceSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Device
        fields = ['id', 'company', 'name', 'model', 'MAC_Address']
        

class DeviceAllocationSerializer(serializers.ModelSerializer):
    device = serializers.StringRelatedField()
    employee = serializers.StringRelatedField()
    class Meta:
        model = DeviceAllocation
        fields = ['id', 'device', 'employee', 'start_date', 'end_date']

    #check that device and employee are belongs to the same company or not.
    def create(self, validated_data):
        device = validated_data['device']
        employee = validated_data['employee']

        if device.company != employee.company:
            raise serializers.ValidationError("Cannot allocate a device from another company.")

        return super().create(validated_data)

    def update(self, instance, validated_data):
        device = validated_data.get('device', instance.device)
        employee = validated_data.get('employee', instance.employee)

        if device.company != employee.company:
            raise serializers.ValidationError("Cannot allocate a device from another company.")

        return super().update(instance, validated_data)
    
    #check that the device is allocated to the employee previously
    def validate(self, attrs):
        device = attrs.get('device')
        employee = attrs.get('employee')

        if DeviceAllocation.objects.filter(device=device, employee=employee).exists():
            raise serializers.ValidationError("This device is already allocated to the employee.")



class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    device_allocation_employee = DeviceAllocationSerializer(many=True, read_only=True)
    class Meta:
        model = Employee
        fields = '__all__'
 #here, I will create a new user which will make connection with company
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        employee = Employee.objects.create(user=user, **validated_data)
        return employee
 
    
    
class CompanySerializer(serializers.ModelSerializer):
    employees = EmployeeSerializer(many=True, read_only=True)
    devices = DeviceSerializer(many=True, read_only=True)
    class Meta:
        model = Company
        fields = '__all__'