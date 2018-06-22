from django.db import models
from django.urls import reverse
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _



class TimeStampedModel(models.Model):

    """Base model"""

    created_at = models.DateField(auto_now_add=True) #게시 시간 추가
    updated_at = models.DateField(auto_now=True) #수정 시간 새로고침

    class Meta:

        abstract = True


class Image(TimeStampedModel):

    """Image model"""

    file = models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField()


class Comment(TimeStampedModel):

    """Comment model"""

    message = models.TextField()


