from django.contrib import admin

from . import models

class AlbumsAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(models.Albums, AlbumsAdmin)