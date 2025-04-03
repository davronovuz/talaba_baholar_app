from django.contrib import admin
from .models import CustomUser

#oddiy
# admin.site.register(CustomUser)

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["id","username","first_name","last_name","email","phone"]
    list_filter = ["first_name","last_name"]
    search_fields = ["username","phone"]


