from django.contrib import admin

from .models import Lifestyle, Lifestyle_detail ,Portrait ,Portrait_detail


admin.site.register(Portrait)
admin.site.register(Portrait_detail)
admin.site.register(Lifestyle)
admin.site.register(Lifestyle_detail)
