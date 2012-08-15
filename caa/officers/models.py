from django.db import models
import itertools

class Officer(models.Model):
    name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50, blank=True)
    picture_filename = models.CharField(max_length=50, blank=True)
    title = models.CharField(max_length=50, blank=True)
    department = models.ForeignKey('Department')
    is_head = models.BooleanField(default=False)
    
    def __unicode__(self):
        return u'%s "%s" (%s)' % (self.name, self.nickname, self.department.name)
    
    class Meta:
        ordering = ['department', '-is_head', 'title', 'name', 'nickname']

class Department(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        
    def get_officers(self):
        officers = Officer.objects.filter(department__exact=self)
        return officers
