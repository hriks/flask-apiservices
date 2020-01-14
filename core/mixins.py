from flask_restful import Resource, reqparse
from flask import request


class APIRestful(Resource):

    def __init__(self):
        if hasattr(self, 'serializer_class'):
            self.serializer = self.serializer_class(data=self.data)
        super().__init__()

    @property
    def data(self):
        return request.json


class ModelSerializer(reqparse.RequestParser):
    MISSING_FILDS_ERROR = '{field} is required.'
    LOCATION = 'json'

    def __init__(self, data=None, instance=None):
        super().__init__()
        for field_name in self.get_fields('read_only_fields'):
            field = getattr(self, field_name)
            self.add_argument(
                field_name, type=field['_type'],
                required=field.get('required'),
                help=self.MISSING_FILDS_ERROR.format(field=field_name),
                location=self.LOCATION)
        self.instance = instance
        self.initial_data = data

    def get_fields(self, field_type=None):
        excl = getattr(
            self.Meta, field_type) if hasattr(self.Meta, field_type) else []
        return [field for field in self.Meta.fields if field not in excl]

    def is_valid(self, strict=False):
        self.parse_args(strict=strict)
        return True

    def save(self):
        self.instance = getattr(
            self, 'update' if self.instance else 'create')(**self.initial_data)

    def create(self, **kwargs):
        instance = self.Meta.model(**kwargs)
        instance.save()
        return instance

    def update(self, **kwargs):
        raise Exception('Not Implemented.')

    @property
    def data(self):
        self._data = dict()
        for field in self.get_fields('write_only_fields'):
            self._data[field] = getattr(self.instance, field)
        return self._data


class ModelException(Exception):
    pass
