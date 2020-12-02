from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Employee)
admin.site.register(Branch)
admin.site.register(Package)
admin.site.register(Tour)


admin.site.register(Client)

admin.site.site_header = "Nesara tours"