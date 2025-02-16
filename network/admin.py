from django.contrib import admin
from django.utils.html import format_html

from .models import NetworkNode, Product


@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "country",
        "city",
        "street",
        "house_number",
        "supplier_link",
        "debt",
        "created_at",
    )
    search_fields = ("name", "email", "city", "country")
    list_filter = ("city",)
    actions = ["clear_debt"]

    def supplier_link(self, obj):
        return format_html(
            '<a href="{}">{}</a>',
            obj.supplier.get_admin_url(),
            obj.supplier.name,
        )

    supplier_link.short_description = "Поставщик"

    def clear_debt(self, request, queryset):
        queryset.update(debt=0)

    clear_debt.short_description = "Очистить задолженность перед поставщиком"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "model", "release_date", "network_node")
    search_fields = ("name", "model")
