from django.db import models
import datetime, os, imghdr
from caa.marathons.models import Marathon

class Building(models.Model):
    name = models.CharField(max_length=50, unique=True)
    map_url = models.CharField(max_length=300, blank=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
    
class Location(models.Model):
    room_number = models.IntegerField()
    building = models.ForeignKey(Building)
    
    def __unicode__(self):
        return u'%s %d' % (self.building, self.room_number)
    
    class Meta:
        ordering = ['building', 'room_number']
        unique_together = ('building', 'room_number')

class Showing(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=100)
    location = models.ForeignKey(Location, blank=True, null=True)
    start_time = models.TimeField(default=datetime.time(19, 00))
    end_time = models.TimeField(default=datetime.time(22, 00))
    schedule = models.ForeignKey('Schedule')
    
    def __unicode__(self):
        return self.title

    def get_preview_folder(self):
        return self.date.strftime('%Y-%m-%d')

    def get_internal_preview_folder(self):
        preview_root_folder = u'/home/calanime/public_html/caa/images/previews'
        return os.path.join(preview_root_folder, self.date.strftime('%Y-%m-%d'))
    
    def get_preview_filenames(self):
        preview_folder_path = self.get_internal_preview_folder()
        preview_filenames = []
        
        if os.path.isdir(preview_folder_path):
            for filename in os.listdir(preview_folder_path):
                if imghdr.what(os.path.join(preview_folder_path, filename)) is not None:
                    #filename is an image
                    preview_filenames.append(filename)
        
        return preview_filenames
    
    class Meta:
        ordering = ['date']
        unique_together = ['schedule', 'date']

class Weekly(models.Model):
    title = models.CharField(max_length=100)
    schedule = models.ForeignKey('Schedule')
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ['schedule', 'title']
        unique_together = ['schedule', 'title']
        verbose_name_plural = "weeklies"

class Schedule(models.Model):
    SEMESTER_CHOICES = (
        (u'FA', u'Fall'),
        (u'SP', u'Spring'),
    )

    year = models.IntegerField()
    semester = models.CharField(max_length=2, choices = SEMESTER_CHOICES)
    
    def __unicode__(self):
        return u'%d %s' % (self.year, self.get_semester_display())
        
    def has_marathon(self):
        marathon = Marathon.objects.filter(year__exact=self.year).filter(semester__exact=self.semester)
        if len(marathon):
            self.marathon = marathon[0]
            return self.marathon
        else:
            self.marathon = None
            return None
    
    class Meta:
        ordering = ['-year', 'semester']
        unique_together = ['year', 'semester']
