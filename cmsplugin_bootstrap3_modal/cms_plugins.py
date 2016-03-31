from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import ModalContainer, ModalPreview, ModalContent, ModalTitle, ModalFooter

class ModalContainerPlugin(CMSPluginBase):
    model = ModalContainer
    render_template = "cmsplugin_bootstrap3_modal/plugin_container.djhtml"
    cache = True
    module = 'Bootstrap Modal'
    name = _('Modal Container')
    allow_children = True
    child_classes = ['ModalPreviewPlugin', 'ModalContentPlugin', 'ModalTitlePlugin', 'ModalFooterPlugin']
    
class ModalPreviewPlugin(CMSPluginBase):
    model = ModalPreview
    render_template = "cmsplugin_bootstrap3_modal/child.djhtml"
    cache = True
    module = 'Bootstrap Modal'
    name = _('Preview Container')
    require_parent = True
    parent_classes = ['ModalContainerPlugin']
    allow_children = True

class ModalContentPlugin(CMSPluginBase):
    model = ModalContent
    render_template = "cmsplugin_bootstrap3_modal/child.djhtml"
    cache = True
    module = 'Bootstrap Modal'
    name = _('Content Container')
    require_parent = True
    parent_classes = ['ModalContainerPlugin']
    allow_children = True

class ModalTitlePlugin(CMSPluginBase):
    model = ModalTitle
    render_template = "cmsplugin_bootstrap3_modal/child.djhtml"
    cache = True
    module = 'Bootstrap Modal'
    name = _('Title Container')
    require_parent = True
    parent_classes = ['ModalContainerPlugin']
    allow_children = True

class ModalFooterPlugin(CMSPluginBase):
    model = ModalFooter
    render_template = "cmsplugin_bootstrap3_modal/child.djhtml"
    cache = True
    module = 'Bootstrap Modal'
    name = _('Footer Container')
    require_parent = True
    parent_classes = ['ModalContainerPlugin']
    allow_children = True
    
plugin_pool.register_plugin(ModalContainerPlugin)
plugin_pool.register_plugin(ModalPreviewPlugin)
plugin_pool.register_plugin(ModalContentPlugin)
plugin_pool.register_plugin(ModalTitlePlugin)
plugin_pool.register_plugin(ModalFooterPlugin)