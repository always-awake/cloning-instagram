from rest_framework import serializers
from . import models
from nomadgram3.users import serializers as user_serializers
from nomadgram3.images import serializers as images_serializers

class NotificationSerializer(serializers.ModelSerializer):

    creator = user_serializers.ListUserSerializer()
    image = images_serializers.SmallImageSerializers()

    class Meta:
        model = models.Notification
        fields = '__all__'