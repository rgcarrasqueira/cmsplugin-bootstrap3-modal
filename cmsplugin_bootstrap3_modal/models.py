from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

from django.db import models

# Create your models here.
class ModalContainer(CMSPlugin):
    title = models.CharField(verbose_name=_('Title'), max_length=60, blank=True)
    
    top = models.CharField(verbose_name='Top', max_length=20, blank=True)
    size = models.CharField(choices=(('sm', _('Small')), ('md', _('Medium')), ('lg', _('Large'))),
                            max_length=2, default='md', blank=True, verbose_name=_('Modal window size'))
    
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