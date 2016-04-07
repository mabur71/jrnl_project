from django.contrib import admin

# Register your models here.
from blog.models import Sites
from blog.models import Records

class SitesAdmin(admin.ModelAdmin):
    pass
admin.site.register(Sites, SitesAdmin)
#admin.site.register(Sites)





admin.site.register(Records)
