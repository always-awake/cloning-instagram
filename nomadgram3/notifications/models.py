from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from nomadgram3.users import models as user_models
from nomadgram3.images import models as image_models


@python_2_unicode_compatible
class Notification(image_models.TimeStampedModel):

    TYPE_CHOICE = (
        ('like', 'Like'),
        ('comment', 'Comment'),
        ('follow', 'Follow'),
    )

    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE, related_name='notifications_creator')
    to = models.ForeignKey(user_models.User, on_delete=models.CASCADE, related_name='notifications_to')
    notifications_type = models.CharField(max_length=20, choices=TYPE_CHOICE)
    image = models.ForeignKey(image_models.Image, on_delete=models.CASCADE, null=True, blank=True, related_name='notifications_image')
    comment = models.ForeignKey(image_models.Comment, on_delete=models.CASCADE, null=True, blank=True, related_name='notifications_comment')