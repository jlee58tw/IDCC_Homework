from django.contrib import admin
from job.models import Document

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id','jobname','datetime')

admin.site.register(Document,DocumentAdmin)
