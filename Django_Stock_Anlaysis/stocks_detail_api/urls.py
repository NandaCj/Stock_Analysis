from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('short-balance-sheet/', views.ShortBalanceSheetApi.as_view(), name='balance_sheet_api'),
]
