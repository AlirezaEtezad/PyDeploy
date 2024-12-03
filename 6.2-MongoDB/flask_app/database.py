from mongoengine import connect, Document, StringField, IntField, FloatField

# Connect to MongoDB
connect(
    db="real_estate",       
    host="mongo",           
    port=27017,             
)

class User(Document):
    username = StringField(required=True, unique=True)
    password = StringField(required=True)

class House(Document):
    district = StringField(required=True)
    rooms = IntField(required=True)
    area = IntField(required=True)
    