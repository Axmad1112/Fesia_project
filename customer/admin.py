from django.contrib import admin
from .models import *


admin.site.register(User)

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
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

admin.site.register(Profile, ProfileAdmin)