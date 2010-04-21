from django.contrib import admin

from thealternativemedicinecabinet.content.models import HealthTip

class HealthTipAdmin(admin.ModelAdmin):
    pass
admin.site.register(HealthTip, HealthTipAdmin)
