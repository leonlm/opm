from rest_framework import viewsets
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authtoken.models import Token
from account.models import AuthUsers


class AccountTokenViewSet(viewsets.ViewSet):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def create(self, request):
        instance = AuthUsers.objects.get(username=request.data['username'])
        token, _ = Token.objects.get_or_create(user=instance)
        data = {
            "code":20000,
            "data": {
                "token": token.key
            }
        }
        return JsonResponse(data, status=status.HTTP_200_OK)
