from django.contrib import admin

from .models import Expense, Type


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "note", "amount", "created_at",)


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at",)
