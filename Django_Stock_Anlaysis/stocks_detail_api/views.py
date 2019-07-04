from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import (BalanceSheetModel, )
from .serializers import (BalanceSheetSerializer, )


class BalanceSheetApi(generics.RetrieveAPIView):

    queryset = BalanceSheetModel.objects.all()
    serializer_class = BalanceSheetSerializer
    lookup_field = 'stock_name'
    # def get(self, request, *args, **kwargs):
    #     print(request, args, kwargs)
    #     return Response({'Success'}, status=200)

