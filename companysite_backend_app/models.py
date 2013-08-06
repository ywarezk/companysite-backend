'''
contains the db models
Created on June 21, 2013

@author: Yariv Katz
@version: 1.0
@copyright: nerdeez.com
'''

#===============================================================================
# begin imports
#===============================================================================

from django.db import models
import datetime
from django.db.models import Q

#===============================================================================
# end imports
#===============================================================================

#===============================================================================
# begin models abstract classes
#===============================================================================

class NerdeezModel(models.Model):
    '''
    this class will be an abstract class for all my models
    and it will contain common information
    '''
    creation_date = models.DateTimeField(default=lambda: datetime.datetime.now().replace(microsecond=0))
    modified_data = models.DateTimeField(default=lambda: datetime.datetime.now().replace(microsecond=0), auto_now=True)
    
    class Meta:
        abstract = True
        
        
#===============================================================================
# end models abstract classes
#===============================================================================

#===============================================================================
# begin tables - models
#===============================================================================

    
class Flatpage(NerdeezModel):
    '''
    the flatpage table
    '''
    title = models.CharField(max_length=250, blank=False, null=False, unique=True)
    html = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.title
        
class Gallery(NerdeezModel):
    '''
    product gallery
    '''
    title = models.CharField(max_length=255, blank=False, null=False, unique=True)
    technologies = models.CharField(max_length=1000, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    html = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='gallery_images', default=None, null=True, blank=True)
    
    def __unicode__(self):
        return self.title
    
class Workers(NerdeezModel):
    '''
    the employees of nerdeez
    '''
    name = models.CharField(max_length=255, blank=False, null=False)
    position = models.CharField(max_length=1000, blank=False, null=False)
    image = models.ImageField(upload_to='workers_images', default=None, null=True, blank=True)
    html = models.TextField(blank=True, null=True)
    
    def __unicode__(self):
        return self.name
    
        

#===============================================================================
# end tables - models
#===============================================================================