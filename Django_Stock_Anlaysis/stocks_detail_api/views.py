from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import (BalanceSheetModel, ShortBalanceSheetModel )
from .serializers import (BalanceSheetSerializer, ShortBalanceSheetSerializer)


class ShortBalanceSheetApi(generics.ListAPIView):

    serializer_class = ShortBalanceSheetSerializer
    filterset_fields = ('stock_name', 'year')

    def get_queryset(self):
        return ShortBalanceSheetModel.objects.all()