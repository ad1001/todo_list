from django.db import models
from datetime import datetime
# Create your models here.
class List(models.Model):
    text = models.CharField(max_length= 200)
    date = models.DateTimeField("Date published",default = datetime.now())
    completed = models.BooleanField(default = False)

    def __str__(self):
        return self.text