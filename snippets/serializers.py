from rest_framework import serializers
from snippets.models import Profile, LANGUAGE_CHOICES, STYLE_CHOICES


class ProfileSerializer(serializers.Serializer):

    type = serializers.CharField(required=False, allow_blank=True, max_length=100)
    name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    description = serializers.CharField(required=False, allow_blank=True, max_length=100)
    
    def create(self, validated_data):
        """Create and return a new profile instance given the validated data"""
        return Profile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """Update and return an existing `Profile` instance, given the validated data."""
        instance.type = validated_data.get('type', instance.type)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
    
    # def delete(self, validated_data):
    #     return Profile.objects.delete(**validated_data)

    # def read(self, validated_data):
    #     return Profile.objects.read(**validated_data)