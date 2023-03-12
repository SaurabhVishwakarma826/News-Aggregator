from django.contrib import admin
from home.models import HomeNews, SportsNews, BusinessNews, WorldNews, PoliticsNews, Contact

# Register your models here.
admin.site.register(HomeNews)
admin.site.register(SportsNews)
admin.site.register(BusinessNews)
admin.site.register(WorldNews)
admin.site.register(PoliticsNews)
admin.site.register(Contact)