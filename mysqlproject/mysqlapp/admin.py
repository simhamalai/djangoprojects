from django.contrib import admin
from mysqlapp.models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','eno','ename','esal','emobile','eemail','eaddress']
admin.site.register(Employee,EmployeeAdmin)
