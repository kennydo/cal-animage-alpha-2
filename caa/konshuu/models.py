from django.db import models

class KonshuuEdition(models.Model):
    volume = models.IntegerField()
    issue = models.IntegerField()

    def __unicode__(self):
        return u'Volume %d Issue %d' % (self.volume, self.issue)

    class Meta:
        ordering = ['-volume', '-issue']