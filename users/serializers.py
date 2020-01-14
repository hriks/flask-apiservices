from core.mixins import ModelSerializer
from users.models import User


class UserSerializer(ModelSerializer):
    email = dict(_type=str, required=True)
    password = dict(_type=str, required=True)
    full_name = dict(_type=str, required=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'full_name')
        write_only_fields = ('password',)
        read_only_fields = ('id',)


class LoginSerializer(ModelSerializer):
    email = dict(_type=str, required=True)
    password = dict(_type=str, required=True)

    class Meta:
        model = User
        fields = ('email', 'password')

    def is_valid(self, strict=False):
        super().is_valid(strict)
        self.instance = self.Meta.model.authenticate(**self.initial_data)
        if self.instance:
            return True
        return False

    def authenticate(self):
        self.instance = self.Meta.model.authenticate(**self.initial_data)
        return self.instance

    def generate_auth_token(self):
        return self.instance.generate_auth_token().decode('utf-8')
