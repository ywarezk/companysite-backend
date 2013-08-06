'''
will hold the admin interface models
Created on Jun 20, 2013

@author: Yariv Katz
@version: 1.0
@copyright: nerdeez.com
'''

#===============================================================================
# begin imports
#===============================================================================
from django.contrib import admin
from companysite_backend_app.models import *

#===============================================================================
# end imports
#===============================================================================

#===============================================================================
# begin admin models
#===============================================================================


class FlatpageAdmin(admin.ModelAdmin):
    pass

class GalleryAdmin(admin.ModelAdmin):
    pass

class WorkersAdmin(admin.ModelAdmin):
    pass


#===============================================================================
# end admin models
#===============================================================================

#===============================================================================
# begin admin site regitration
#===============================================================================

admin.site.register(Flatpage, FlatpageAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Workers, WorkersAdmin)


#===============================================================================
# end admin site registration
#===============================================================================