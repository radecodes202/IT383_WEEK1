from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.models import *

# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(Asset)
admin.site.register(Organization)
admin.site.register(Project)
admin.site.register(LeaveRequest)
admin.site.register(Product)
admin.site.register(Warehouse)
admin.site.register(StockMovement)
# admin.site.register(TimeStampedModel)
