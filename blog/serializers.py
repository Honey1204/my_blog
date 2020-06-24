from rest_framework import serializers
from blog import models

class PostSerializer(serializers.ModelSerializer):

	class Meta:
		model = models.Post
		fields = ['title','category','date_published','author','id']



class PostDetailSerializer(serializers.ModelSerializer):

	class Meta:
		model = models.Post
		fields = ['title','category','date_published','content','author','id']

class PostCreateSerializer(serializers.ModelSerializer):

	class Meta:
		model = models.Post
		fields = ['title','category','date_published','content','author']


# class UserProfileSerializer(serializers.ModelSerializer):


# 	class Meta:
# 		model = models.UserProfile

# 	def create(self, validated_data):

# 		return models.UserProfile.objects.create_user(
#         username=validated_data['username'],
#         email=validated_data['email'],
#  		password=validated_data['password'],
#  		nick_name=validated_data['nick_name'],
#     )

# 	