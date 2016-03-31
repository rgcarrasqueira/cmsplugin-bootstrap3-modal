from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

from django.db import models

# Create your models here.
class ModalContainer(CMSPlugin):
    title = models.CharField(verbose_name=_('Title'), max_length=60, blank=True)
    
    classes = models.TextField(verbose_name=_('Classes'), blank=True)
    
    def __str__(self):
        if self.title:
            return self.title
        else:
            return CMSPlugin.__str__(self)
        
class ModalPreview(CMSPlugin):
    pass

class ModalContent(CMSPlugin):
    pass

class ModalTitle(CMSPlugin):
    pass

class ModalFooter(CMSPlugin):
    pass