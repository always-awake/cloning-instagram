from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers


class Feed(APIView):

    def get(self, request, format=None):

        user = request.user

        following_users = user.following.all()

        #사용자가 following 하는 users의 최근 사진 2장을 저장하기 위한 배열 생성
        image_list = []

        print(following_users)

        for following_user in following_users:

            user_images = following_user.images.all()[:2]

            for image in user_images:

                image_list.append(image)

        sorted_list = sorted(
            image_list, key=lambda image:image.created_at, reverse=True)

        serializer = serializers.ImageSerializer(sorted_list, many=True)

        return Response(serializer.data)

