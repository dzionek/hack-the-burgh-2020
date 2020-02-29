from django.db import models
import json

# Create your models here.
from django.contrib.auth.models import User

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    has_coronavirus = models.BooleanField(default=False)
    places_list = models.TextField(default='[]')

    @property
    def list(self):
        return json.loads(self.places_list)

    @list.setter
    def list(self, value):
        self.places_list = json.dumps(self.list + value)