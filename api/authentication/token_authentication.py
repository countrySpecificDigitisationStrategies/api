from rest_framework.authentication import BaseAuthentication

from api.models import Token


class TokenAuthentication(BaseAuthentication):

    def authenticate(self, request):
        code = request.META.get('HTTP_AUTHORIZATION')

        if not code:
            return None

        if len(code) != 36:
            return None

        try:
            token = Token.objects.get(code=code)
        except:
            return None

        if not token.user.is_active:
            return None

        return (token.user, token)
