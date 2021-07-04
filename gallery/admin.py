from django.contrib import admin
from gallery.models import Image

# Register your models here.
# admin.site.register((Image))
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['sno', 'image', 'desc', 'timeStamp']