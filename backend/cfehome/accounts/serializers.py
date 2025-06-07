# accounts/serializers.py
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from accounts.models import StaffRegistry

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
    staff_number = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'username', 
            'email', 
            'password',
            'staff_number',
        ]

    def validate_staff_number(self, value):
        try:
            staff = StaffRegistry.objects.get(staff_number=value)
        except StaffRegistry.DoesNotExist:
            raise serializers.ValidationError("Invalid staff number.")

        if staff.is_used in ['t', True]:
            raise serializers.ValidationError("This staff number has already been used.")

        return value

    def create(self, validated_data):
        staff_number = validated_data.pop('staff_number')
        password = validated_data.pop('password')

        user = User(**validated_data)
        user.set_password(password)
        user.is_staff = True
        user.save()

        # Add user to Staff group
        staff_group = Group.objects.get(name='Staff')
        user.groups.add(staff_group)

        # Mark staff_number as used
        staff = StaffRegistry.objects.get(staff_number=staff_number)
        staff.is_used = 't'  # mark as used
        staff.save()

        return user