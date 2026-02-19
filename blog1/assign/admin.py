from django.contrib import admin
from .models import About, FollowUs

# Register your models here.
class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Limit to only one instance
        if About.objects.exists():
            return False
        return super().has_add_permission(request)

admin.site.register(About, AboutAdmin)
admin.site.register(FollowUs)

