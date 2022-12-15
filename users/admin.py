from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        ("Profile",
         {
             "fields": ("username", "password", "name", "email", "is_host")
         },
         ),
        # 필요한 것들은 UserAdmin에서 더 가져올 수 있다.
        # Document에 더욱 더 많은 것들이 존재한다!
    )
    # 이렇게도 할 수 있다.
    # fields = ("email", "password", "name")
    # 이런식으로 할 수도 있고, 딕셔너리처럼 할 수도 있다.

    list_display = ("username", "email", "name", "is_host",)
