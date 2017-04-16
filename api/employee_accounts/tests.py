# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.test import TestCase

from rest_framework.test import APITestCase

from .models import EmployeeAccount, EmployeeAccountPosition 
from .serializers import EmployeeAccountSerializer

class EmployeeAccountSerializerTest(APITestCase):
    def setUp(self):
        self.eap_emp = EmployeeAccountPosition.objects.create(position_name='Employee')
        self.eap_manager = EmployeeAccountPosition.objects.create(position_name='Manager')

    def test_invalid_emp_position(self):
        account = User.objects.create_user(username='johndoe')
        account.set_password('johndoejohndoe')
        account.save()
        self.assertTrue(authenticate(username='johndoe', password='johndoejohndoe'))

        ea = EmployeeAccount.objects.create(
                firstname='John',
                lastname='Doe',
                account=account,
                account_position=self.eap_emp,
            )
    #firstname = models.CharField(max_length=64, blank=True)
    #lastname = models.CharField(max_length=64, blank=True)
    #account = models.OneToOneField(User, on_delete=models.CASCADE)
    #account_position = models.ForeignKey(EmployeeAccountPosition, related_name='position')
