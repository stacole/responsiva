from django.contrib import admin
from .models import Resguardos

# Register your models here.
class AdminResguardos(admin.ModelAdmin):
    list_display = ["name", "gid", "department", "position", "device","detail", "signature"]

admin.site.register(Resguardos, AdminResguardos)