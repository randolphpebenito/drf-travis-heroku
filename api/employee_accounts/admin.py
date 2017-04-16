# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import EmployeeAccountPosition, EmployeeAccount

class EmployeeAccountPositionAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'timestamp')

class EmployeeAccountAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'account_position', 'date_modified', 'date_created')

admin.site.register(EmployeeAccountPosition, EmployeeAccountPositionAdmin)
admin.site.register(EmployeeAccount, EmployeeAccountAdmin)
