from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(MeasurementUnit)
admin.site.register(Section)
admin.site.register(Shape)
admin.site.register(Code)
admin.site.register(ItemName)
admin.site.register(RawMaterial)
admin.site.register(Machine)
admin.site.register(RawMaterialIncoming)
admin.site.register(RawMaterialOutgoing)
admin.site.register(MachineCapacity)
admin.site.register(JiggerProduction)
