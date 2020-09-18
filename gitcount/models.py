from django.db import models
from django.contrib.auth.models import User

class CountModel(models.Model):
    gitid = models.CharField(max_length=100)
    gitcommitcount = models.CharField(max_length=400)

    def __str__(self):
        return "%s - %s" % (self.gitid, self.gitcommitcount)