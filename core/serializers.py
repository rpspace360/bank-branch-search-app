from rest_framework import serializers

from core.models import Branch, Bank


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'
     

class BranchSerializer(serializers.ModelSerializer):

    bank_name = serializers.CharField(source='bank.name',
                                      read_only=True)
    class Meta:
        model = Branch
        fields = '__all__'
       
