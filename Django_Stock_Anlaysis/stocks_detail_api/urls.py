from django.contrib import admin
from django.urls import path
from .views import BalanceSheetApi

urlpatterns = [
    path('balancesheet/<int:stock_name>', BalanceSheetApi.as_view(), name='balance_sheet_api'),
]
