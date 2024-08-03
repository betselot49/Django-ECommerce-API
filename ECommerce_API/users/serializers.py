from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):

    user = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)

    class Meta:
        model = Profile
        fields = ['url', 'id', 'user', 'image']

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, required=False, style={'input_type': 'password'})
    username = serializers.CharField(read_only=True)
    old_password = serializers.CharField(write_only=True, required=False, style={'input_type': 'password'})
    profile = ProfileSerializer(required=False, read_only=True)

    def validate(self, data):
        request_method = self.context['request'].method
        if request_method == 'POST':
            if not data.get('password'):
                raise serializers.ValidationError({"message": "Password field is required"})
        elif request_method == "PUT" or request_method == "PATCH":
            if not data.get('password') and not data.get('old_password'):
                raise serializers.ValidationError({"message": "Password and old password fields are required"})

        return super().validate(data)
        

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        return user
    

    def update(self, instance, validated_data):
        try:
            user = instance
            if 'password' in validated_data:
                password = validated_data.pop('password')
                old_password = validated_data.pop('old_password')

                if user.check_password(old_password):
                    user.set_password(password)
                else:
                    raise Exception('Old password is incorrect')
                user.save()

        except Exception as err:
            raise serializers.ValidationError({"message": err})
        
        return super().update(instance, validated_data)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'first_name', 'last_name', 'password', 'old_password', 'profile']