from django.contrib import admin
from .models import House

# 이 @을 통해, 이 HouseAdmin이 House클래스를 조작한다는 것을 선언한다.
@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
	list_display = (
		"name",
		"price_per_night",
		"address",
		"pets_allowed",
	)
	list_filter = ("price_per_night", "pets_allowed")
	search_fields = ("address",)