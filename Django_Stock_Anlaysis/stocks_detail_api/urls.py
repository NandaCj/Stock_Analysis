from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('balancesheet/<int:id>', views.Test_BalanceSheetApi.as_view(), name='balance_sheet_api'),
]
