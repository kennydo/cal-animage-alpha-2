from django.db import models

class Event(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    marathon = models.ForeignKey('Marathon')
    title = models.CharField(max_length=100)
    
    def __unicode(self):
        return u'%d %s - %s' % (self.marathon.year, self.marathon.get_semester_display(), self.title)
    
    class Meta:
        ordering = ['-marathon', 'start_time']
        unique_together = ['marathon', 'start_time']

class Marathon(models.Model):
    SEMESTER_CHOICES = (
        (u'FA', u'Fall'),
        (u'SP', u'Spring'),
    )

    year = models.IntegerField()
    semester = models.CharField(max_length=2, choices = SEMESTER_CHOICES)
    
    date = models.DateField(blank=True, null=True)
    location = models.ForeignKey('schedules.Location', blank=True, null=True)
    
    def get_events(self):
        return Event.objects.filter(marathon__exact=self)
    
    def __unicode__(self):
        return u'%d %s' % (self.year, self.get_semester_display())
    
    class Meta:
        ordering = ['-year', '-semester']
        unique_together = ['year', 'semester']

