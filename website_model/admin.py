from django.contrib import admin
#from django.models import
# Register your models here.
from website_model.models import Member,ordr,Groop
admin.site.register(Member)
admin.site.register(Groop)
admin.site.register(ordr)
