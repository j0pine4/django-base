from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers

""" 
Serializers for the user API 
"""

class UserSerializer(serializers.ModelSerializer):
    """ Serializer for the User object"""

    class Meta:
        model = get_user_model()
        fields = [
            'email',
            'password',
            'firstName',
            'lastName',
        ]
        extra_kwargs = {
            'password': {
                'write_only': True, 
                'min_length': 5
                }
            }

    def create(self, validated_data):
        """ Create and return user with encrypted password """
        return get_user_model().objects.create_user(**validated_data)
    