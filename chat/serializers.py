from rest_framework import serializers

from .models import Message,User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id','username']


class MessageSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    class Meta: 
        model = Message
        fields = ["id","message","created_at","updated_at","created_by"]
    