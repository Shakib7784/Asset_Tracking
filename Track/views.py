from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import CompanySerializer, EmployeeSerializer, UserSerializer,DeviceSerializer, DeviceAllocationSerializer
from .models import Company, Employee, Device,DeviceAllocation,DeviceLog
import datetime

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @action(detail=True, methods=['POST'])
    # to add user from company we need to visit companies/company_id. Then we will get add employee option
    def add_employee(self, request, pk=None):
        company = self.get_object()
        username = request.data.get('username')
        password = request.data.get('password')

        # Create user account
        user_serializer = UserSerializer(data={'username': username, 'password': password})
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()

        # Create employee and associate with company
        employee = Employee.objects.create(user=user, company=company)
        employee_serializer = EmployeeSerializer(employee)

        return Response(employee_serializer.data, status=status.HTTP_201_CREATED)
    
    
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    
    

class DeviceAllocationViewSet(viewsets.ModelViewSet):
    queryset = DeviceAllocation.objects.all()
    serializer_class = DeviceAllocationSerializer


# class DeviceLogViewSet(viewsets.ModelViewSet):
#     queryset = DeviceLog.objects.all()
#     serializer_class = DeviceLogSerializer
    
    