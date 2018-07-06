from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers

class Explore(APIView):

    def get(self, request, format=None):

        users = models.User.objects.all()

        serializer = serializers.ExploreUserSerializer(users, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class FollowUser(APIView):

    def post(self, request, user_id, format=None):

        user = request.user

        try:
            user_to_follow = models.User.objects.get(id=user_id)
        except models.User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        user.following.add(user_to_follow)

        user.save()
        
        user_to_follow.followers.add(user)

        user_to_follow.save()
        
        return Response(status=status.HTTP_200_OK)
