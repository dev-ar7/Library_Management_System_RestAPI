from django.contrib import admin
from django.contrib.auth.models import Group


admin.site.unregister(Group)


admin.site.site_header  =  "Library admin"  
admin.site.site_title  =  "Library admin site"
admin.site.index_title  =  "Library Admin"