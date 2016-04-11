from django.contrib import admin

# Register your models here.
from blog.models import Sites
from blog.models import Records

class SitesAdmin(admin.ModelAdmin):
    list_display = ('printout',) 

admin.site.register(Sites, SitesAdmin)
#admin.site.register(Sites)



class RecordsAdmin(admin.ModelAdmin):
    def site_printout(self, obj):
        return obj.site.printout
    site_printout.short_description = 'Station'
    list_display = ('date', 'site', 'text','person',)
    list_filter = ('site','person',)
    search_fields = ['text']
    list_editable = ('text', 'person')
    #list_select_related = ('site',)
    #list_select_related = True 

admin.site.register(Records, RecordsAdmin)
#admin.site.register(Records)
