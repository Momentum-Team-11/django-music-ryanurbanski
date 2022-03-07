from django.contrib import admin

from . import models

class AlbumsAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Albums, AlbumsAdmin)