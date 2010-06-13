from django.contrib import admin

from thealternativemedicinecabinet.content.models import HealthTip, UpcomingEvent, RecommendedResource, Media, Email

class HealthTipAdmin(admin.ModelAdmin):
    pass
admin.site.register(HealthTip, HealthTipAdmin)

class UpcomingEventAdmin(admin.ModelAdmin):
    pass
admin.site.register(UpcomingEvent, UpcomingEventAdmin)

class RecommendedResourceAdmin(admin.ModelAdmin):
    pass
admin.site.register(RecommendedResource, RecommendedResourceAdmin)

class MediaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Media, MediaAdmin)

class EmailAdmin(admin.ModelAdmin):
    pass
admin.site.register(Email, EmailAdmin)
