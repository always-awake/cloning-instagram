from django.contrib import admin
from . import models

#해당 모델을 admin 패널에 register해주는 역할의 데코레이션
@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
#이 클래스는 모델들이 어드민패널에서 어떻게 보이게 될지 결정해주는 클래스이다.

    #해당 오브젝트 편집(수정)화면으로 가는 링크를 걸어놓을 필드 설정
    list_display_links = (
        'location',
    )

    list_filter = (
        'file',
        'location',
        'creator',
    )

    list_display = (
        'id',
        'location',
        'caption',
        'creator',
        'created_at',
        'updated_at',   
    )


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    
    list_display_links = (
        'message',
    )

    list_filter = (
        'image',
        'creator',
    )

    list_display =(
        'message',
        'image',
        'creator',
        'created_at',
        'updated_at',
    )
    

@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):

    list_display_links = (
        'image',
    )

    list_filter = (
        'image',
        'creator',
    )

    list_display = (
        'image',
        'creator',
        'created_at',
        'updated_at',
    )