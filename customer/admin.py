from django.contrib import admin
from .models import *


admin.site.register(User)
admin.site.disable_action('delete_selected')

@admin.action(description='delete selected profiles')
def delete_model(modeladmin, request, queryset):
    
    bank = CoinBase.objects.first()
    for obj in queryset:
        bank.coin+= obj.coin
        obj.delete()
    bank.save()
    
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["email","user","coin","phone_number","first_name"]
    ordering = ['coin']
    actions = ['my_action', 'my_other_action', delete_model]

admin.site.register(Profile, ProfileAdmin)