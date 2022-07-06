from marshmallow import Schema, fields

class RevenueSchema(Schema):
    country = fields.Str()
    source = fields.Str()
    platform = fields.Str()
    device_family = fields.Str()
    event_1 = fields.Float()
    event_2 = fields.Float()