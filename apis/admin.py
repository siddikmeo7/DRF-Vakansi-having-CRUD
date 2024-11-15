from django.contrib import admin
from .models import *


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ["username","email","is_staff",]
    list_filter =  ["username","is_staff"]
    search_fields = ["username",]

@admin.register(Vakansi)
class AdminVakansi(admin.ModelAdmin):
    list_display = ["id","user","title","created_at",]
    list_filter = ["user","title","created_at",]
    search_fields = ["title",]

@admin.register(Request)
class AdminRequest(admin.ModelAdmin):
    search_fields = ["vakansi",]
    list_display = ["vakansi","user","created_at",]
    list_filter = ["vakansi","created_at",]