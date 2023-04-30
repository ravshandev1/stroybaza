from rest_framework import serializers, exceptions
from .models import Account, VerifyPhone, UserCard
from .validators import card_validity_period_validator, card_number_validator


class UserCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCard
        fields = ['user', 'card_number', 'validity_period', 'card_holder']

    def validate(self, attrs):
        num = attrs['card_number']
        mud = attrs['validity_period']
        if card_number_validator(num) is False:
            raise exceptions.ValidationError(
                {'success': False,
                 'message': "Karta raqami noto'g'ri kiritildi\nIltimos faqat Uzcard yoki Humo kartalarini kiriting!"})
        if card_validity_period_validator(mud) is False:
            raise exceptions.ValidationError(
                {'success': False, 'message': "Kartani amal qilish muddati noto'g'ri kiritildi!"})
        return attrs


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'phone']


class VerifySerializer(serializers.ModelSerializer):
    class Meta:
        model = VerifyPhone
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'phone', 'date_birth', 'name', 'email']
