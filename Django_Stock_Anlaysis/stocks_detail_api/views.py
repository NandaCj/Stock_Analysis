from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import (BalanceSheetModel, ShortBalanceSheetModel )
from .serializers import (BalanceSheetSerializer, )


class BalanceSheetApi(generics.RetrieveAPIView):

    serializer_class = BalanceSheetSerializer

    def get_queryset(self):
        return ShortBalanceSheetModel.objects.all()

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response({'No Data for this stock'}, status=200)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class Test_BalanceSheetApi(generics.RetrieveAPIView):

    # queryset = ShortBalanceSheetModel.objects.all()
    serializer_class = BalanceSheetSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return ShortBalanceSheetModel.objects.all()
