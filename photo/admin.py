from django.contrib import admin

from .models import Lifestyle, Lifestyle_detail, Portrait, Portrait_detail, Wedding, Wedding_detail


admin.site.register(Portrait)
admin.site.register(Portrait_detail)
admin.site.register(Lifestyle)
admin.site.register(Lifestyle_detail)
admin.site.register(Wedding)
admin.site.register(Wedding_detail)
