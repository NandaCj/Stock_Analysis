from rest_framework import serializers
from .models import (   BalanceSheetModel,
                        ShortBalanceSheetModel,)

class BalanceSheetSerializer(serializers.ModelSerializer):

    class Meta :
        model = ShortBalanceSheetModel
        fields = '__all__'

class ShortBalanceSheetSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShortBalanceSheetModel
        fields = '__all__'