from rest_framework import serializers
from .models import EmployeeAccount 

class EmployeeAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeAccount
        fields = (
                'firstname',
                'lastname',
                'account',
                'account_position',
            )
