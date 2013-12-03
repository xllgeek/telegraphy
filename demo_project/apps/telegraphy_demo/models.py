from django.db.models import Model, CharField
from telegraphy.contrib.django_telegraphy.events import BaseModelEvent


class MyModel(Model):
    title = CharField(max_length=128)


class MyModelEvents(BaseModelEvent):
    model = MyModel
    fields = ('title', )
    name = 'telegraphy_demo.MyModel'
