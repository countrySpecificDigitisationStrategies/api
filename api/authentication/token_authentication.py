from rest_framework.authentication import BaseAuthentication

from api.models import Token


class TokenAuthentication(BaseAuthentication):

    def authenticate(self, request):
        identifier = request.META.get('HTTP_AUTHORIZATION')

        if not identifier:
            return None

        if len(identifier) != 36:
            return None

        try:
            token = Token.objects.get(identifier=identifier)
        except:
            return None

        if not token.user.is_active:
            return None

        return (token.user, token)
