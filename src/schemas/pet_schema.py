import json
from marshmallow import fields, Schema, EXCLUDE
from src.entities.pet_entity.pet_attributes import petAttributes


# schemas classes , used marshmallow library to Serialize/DeSerialize data .

class Flat_To_Nested(fields.Nested):
    _CHECK_ATTRIBUTE = False

    def _serialize(self, nested_obj, attr, obj):
        return json.loads(self.schema.dumps(obj))

class Flat_To_Nested_Dict(fields.Nested):
    _CHECK_ATTRIBUTE = False

    def _serialize(self, nested_obj, attr, obj):
        return json.loads('['+ self.schema.dumps(obj) + ']')



class tagsSectionSchema(Schema):
    class Meta:
        ordered = True
    id = fields.Integer(attribute=petAttributes.TAGS_ID.value, load_default=0)
    name = fields.Str(attribute=petAttributes.TAGS_NAME.value,load_default='string')

class categorySectionSchema(Schema):
    class Meta:
        ordered = True
    id = fields.Integer(attribute=petAttributes.CATEGORY_ID.value)
    name = fields.Str(attribute=petAttributes.CATEGORY_NAME.value)


class petPostRequestSchema(Schema):
    class Meta:
        ordered = True
    id = fields.Integer(attribute=petAttributes.ID.value)
    category = Flat_To_Nested(categorySectionSchema())
    name = fields.Str(attribute=petAttributes.NAME.value)
    photoUrls = fields.List(fields.String, attribute=petAttributes.PHOTO_URLS.value)
    tags = Flat_To_Nested_Dict(tagsSectionSchema())
    status = fields.Str(attribute=petAttributes.STATUS.value)


class petidSchema(Schema):
    class Meta:
        unknown = EXCLUDE
    id = fields.Integer(attribute=petAttributes.ID.value)
    name = fields.Str(attribute=petAttributes.NAME.value)