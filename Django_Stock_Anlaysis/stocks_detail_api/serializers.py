from rest_framework import serializers
from .models import BalanceSheetModel

class BalanceSheetSerializer(serializers.Serializer):

    class Meta :
        Model = BalanceSheetModel
        fields = '__all__'
