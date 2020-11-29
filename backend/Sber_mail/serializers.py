from rest_framework import serializers
from Sber_mail.models import SberMail

class SberMailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SberMail
        fields = ['id', 'date', 'mail', 'subject', 'text', 'short_text', 'tags', 'priority']

class SberMailListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SberMail
        fields = ['id', 'priority']
    # id = serializers.IntegerField(read_only=True)
    # mail_id = serializers.CharField(max_length=100)
    # date = serializers.CharField(max_length=100)
    # # sender = models.CharField(max_length=100)
    # mail = serializers.CharField(max_length=100)
    # subject = serializers.TextField()
    # text = serializers.TextField(required=False)
    # short_text = serializers.TextField(required=False)
    #
    # def create(self, validated_data):
    #     return SberMail.objects.create(**validated_data)
