from django.contrib import admin
from .models import Department, Designation, Role, Employee

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'responsibilities')
    search_fields = ('name', 'department__name')

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'department', 'designation', 'role', 'is_active')
    list_filter = ('department', 'designation', 'role', 'is_active')
    search_fields = ('first_name', 'last_name', 'email', 'department__name', 'designation__name', 'role__name')