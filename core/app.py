from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

from core.settings import create_app
from users.urls import urls

app = create_app()

app = create_app()
db = SQLAlchemy(app)
api = Api(app)

for k, v in urls:
    api.add_resource(v, k)
