from rest_framework import viewsets
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class AccountInfoViewSet(viewsets.ViewSet):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        data = {
            "code":20000,
            "data": {
                "roles":["admin"],
                "introduction":"I am a super administrator","avatar":"https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif","name":"Super Admin"
            }
        }
        return JsonResponse(data, status=status.HTTP_200_OK)