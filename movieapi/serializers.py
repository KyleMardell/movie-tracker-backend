from rest_framework import serializers
from movieapi.models import Movie
from django.contrib.auth.models import User

class MovieSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    
    def validate(self, data):
        user = self.context['request'].user
        tmdb_id = data.get('tmdb_id')
        queryset = Movie.objects.filter(user=user, tmdb_id=tmdb_id)

        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)

        if queryset.exists():
            raise serializers.ValidationError("You already added this movie.")

        return data
        
    class Meta:
        model = Movie
        fields = [
            'id', 'user', 'title', 'tmdb_id',
            'image_path', 'watched', 'created_on',
        ]
        
        
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'password']
        
    def validate(self, data):
        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError("Username already taken.")
        if not data['password']:
            raise serializers.ValidationError("Password cannot be empty.")
        return data
        
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)