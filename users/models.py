from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from itsdangerous import TimedJSONWebSignatureSerializer

from core.settings import SECRET_KEY

db = SQLAlchemy()
bcrypt = Bcrypt()


class ModelMixin:

    def save(self, *args, **kwargs):
        db.session.add(self)
        db.session.commit()
        return self


class User(db.Model, ModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(48), unique=True)
    full_name = db.Column(db.String(128))
    password = db.Column(db.String(256))

    __tablename__ = 'user'

    def save(self, *args, **kwargs):
        if getattr(self, 'id') is None:
            self.password = self.hash_password()
        super().save(*args, **kwargs)

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def check_password(self, password):
        try:
            return bcrypt.check_password_hash(self.password, str(password))
        except ValueError:
            return False

    def hash_password(self):
        return bcrypt.generate_password_hash(self.password, 6).decode('utf-8')

    @classmethod
    def authenticate(cls, email, password):
        user = cls.query.filter_by(email=email).first_or_404()
        if user.check_password(password):
            return user

    def generate_auth_token(self, expiration=1800):
        s = TimedJSONWebSignatureSerializer(SECRET_KEY, expires_in=expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        s = TimedJSONWebSignatureSerializer(SECRET_KEY)
        data = s.loads(token)
        user = User.query.get(data['id'])
        return user
