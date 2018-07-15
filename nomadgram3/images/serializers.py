from rest_framework import serializers
from . import models
from nomadgram3.users import models as user_models


class SmallImageSerializers(serializers.ModelSerializer):

    class Meta:
        model = models.Image
        fields = (
            'file',
        )
    


class CountImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Image
        fields = (
            'id',
            'file',
            'comment_count',
            'like_count',
        )



class FeedUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.user_models.User
        fields = (
            'profile_image',
            'username',
        )


class CommentSerializer(serializers.ModelSerializer):
    
    creator = FeedUserSerializer(read_only=True)

    class Meta:
        model = models.Comment
        fields = (
            'id',
            'message',
            'creator'
        )


class LikeSerializer(serializers.ModelSerializer):


    class Meta:
        model = models.Like
        fields = '__all__'
      

class ImageSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True)
    creator = FeedUserSerializer()
    
    class Meta:
        model = models.Image
        fields = (
            'id',
            'file',
            'creator',
            'location',
            'caption',
            'comments',
            'like_count', #@property
            'created_at',
        )


