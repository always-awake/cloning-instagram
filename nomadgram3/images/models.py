from django.db import models
from django.urls import reverse
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
# 첫 번째 줄의 models과 이름을 다르게 설정해야한다.
# 이름이 같으면 충돌이 일어난다. 
# user 속 model에는 DateField, CharField 같은 것이 없음
from nomadgram3.users import models as user_models



class TimeStampedModel(models.Model):

    """Base Model"""

    created_at = models.DateField(auto_now_add=True) #게시 시간 추가
    updated_at = models.DateField(auto_now=True) #수정 시간 새로고침

    class Meta:

        abstract = True


class Image(TimeStampedModel):

    """ Image Model """

    file = models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField()
    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE, null=True)


class Comment(TimeStampedModel):

    """ Comment Model """

    message = models.TextField()
    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE, null=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)


class Like(TimeStampedModel):

    """ Like Model """

    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE, null=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)