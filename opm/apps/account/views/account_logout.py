from django.http.response import JsonResponse
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework import status


class AccountLogoutView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        return JsonResponse({"code":20000,"data":{}}, status=status.HTTP_200_OK)
