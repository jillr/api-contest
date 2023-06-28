from django.contrib.auth.models import User
from rest_framework import serializers
from tamagotchi.models import Pet


class PetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Pet
        fields = ['id', 'name', 'fed', 'interacted', 'hungry', 'bored', 'owner']


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Pet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'pet']