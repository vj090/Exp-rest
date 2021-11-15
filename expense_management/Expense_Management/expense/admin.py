from django.contrib import admin
from .models import Expense, Category, ExpenseMonth


@admin.register(Expense)
class Expenses(admin.ModelAdmin):
    list_display = ('user', 'type', 'expense_category')
    list_filter = ['user']


@admin.register(Category)
class Categories(admin.ModelAdmin):
    list_display = ('user', 'name')
    list_filter = ['user']


@admin.register(ExpenseMonth)
class ExpenseMonths(admin.ModelAdmin):
    list_display = ('user', 'name')
    list_filter = ['user']
