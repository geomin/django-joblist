from django.db import models
from lingua import translation

class Job(models.Model):
    class Translation(translation.Translation):
        name = models.CharField(max_length=40, unique=True)

    def __unicode__(self):
        return unicode(self.name) 
