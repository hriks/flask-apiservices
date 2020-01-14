from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound

from core.mixins import APIRestful
from users.serializers import UserSerializer, LoginSerializer
from users.decorators import is_authenticated


class Register(APIRestful):
    serializer_class = UserSerializer

    def post(self, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=self.data)
            serializer.is_valid(strict=True)
            serializer.save()
        except IntegrityError:
            return dict(
                detail="User Already registered with email provided."), 400
        return serializer.data, 201


class Login(APIRestful):
    serializer_class = LoginSerializer

    def post(self, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=self.data)
            if serializer.is_valid(strict=True):
                return dict(
                    token=serializer.generate_auth_token()), 200
            return dict(detail='Invalid email and password combination.'), 400
        except NotFound:
            return {'detail': 'Invalid email provided.'}, 400


class UserDetails(APIRestful):
    method_decorators = [is_authenticated]
    serializer_class = UserSerializer

    def get(self, user, *args, **kwargs):
        serializer = self.serializer_class(instance=user)
        return serializer.data, 200
