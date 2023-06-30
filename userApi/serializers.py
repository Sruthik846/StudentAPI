from rest_framework import serializers
from .models import StudentDetails
from django.contrib.auth.models import User

class StudentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetails
        fields = '__all__'

    # def create(self, validated_data):
    #     user = User.objects.create(
    #         username = validated_data['name']
    #     )
    #     user.save()
    #     return user

