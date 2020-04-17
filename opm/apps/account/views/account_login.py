from django.http.response import JsonResponse
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework import status


class AccountLoginView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        data = serializer.validated_data
        return JsonResponse({"code":20000,"data":{"token": data['access']}}, status=status.HTTP_200_OK)
