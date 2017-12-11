from django.contrib import admin
from accounts.models import Userid

class UseridAdmin(admin.ModelAdmin):
    list_display = ('id','user')

admin.site.register(Userid,UseridAdmin)