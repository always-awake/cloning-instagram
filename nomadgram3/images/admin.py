from django.contrib import admin
from . import models

#해당 모델을 admin 패널에 register해주는 역할의 데코레이션
@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
#이 클래스는 모델들이 어드민패널에서 어떻게 보이게 될지 결정해주는 클래스이다.
    pass


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):

    pass
@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):

    pass