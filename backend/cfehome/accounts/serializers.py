# accounts/serializers.py
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSignupSerializer(serializers.ModelSerializer):
    user_type = serializers.ChoiceField(choices=[
        ('customer', 'Customer'), 
        ('seller', 'Seller')
        ])
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'username', 
            'email', 
            'password', 
            'user_type']

    def create(self, validated_data):
        user_type = validated_data.pop('user_type')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()

        group_name = 'Customer' if user_type == 'customer' else 'Seller'
        group = Group.objects.get(name=group_name)
        user.groups.add(group)

        return user


class StaffSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.is_staff = True
        user.save()

        staff_group = Group.objects.get(name='Staff')
        user.groups.add(staff_group)

        return user
