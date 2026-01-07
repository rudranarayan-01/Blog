from django.contrib import admin

from .models import AboutModel, SocialLinks

class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count = AboutModel.objects.all().count()
        if count == 0:
            return True
        return False
    
# Register your models here.
admin.site.register(AboutModel, AboutAdmin)
admin.site.site_header = "Apex News Admin"
admin.site.site_title = "Apex News Admin Portal"
admin.site.register(SocialLinks)