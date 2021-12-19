from django.contrib import admin
from .models import CoinBase,SpentCoin,EarnCoin
# Register your models here.
admin.site.register(CoinBase)
admin.site.register(SpentCoin)
admin.site.register(EarnCoin)