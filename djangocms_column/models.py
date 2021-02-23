from six import python_2_unicode_compatible

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin

if hasattr(settings, "COLUMN_WIDTH_CHOICES"):
    WIDTH_CHOICES = settings.COLUMN_WIDTH_CHOICES
else:
    WIDTH_CHOICES = (
        ('10%', _("10%")),
        ('25%', _("25%")),
        ('33.33%', _('33%')),
        ('50%', _("50%")),
        ('66.66%', _('66%')),
        ('75%', _("75%")),
        ('100%', _('100%')),
    )

BG_CHOICES = (
    ('has-background-white', _("White")),
    ('has-background-black has-text-white', _("Black")),
    ('has-background-purple has-text-white', _("Purple")),
)

@python_2_unicode_compatible
class MultiColumns(CMSPlugin):
    """
    A plugin that has sub Column classes
    """
    cmsplugin_ptr = models.OneToOneField(
        CMSPlugin,
        related_name='%(app_label)s_%(class)s',
        parent_link=True,
        on_delete=models.CASCADE,
    )
    add_class = models.CharField(
        _("class"),
        max_length=50, null=True, blank=True)

    def __str__(self):
        plugins = self.child_plugin_instances or []
        return _(u"%s columns") % len(plugins)


@python_2_unicode_compatible
class Column(CMSPlugin):
    """
    A Column for the MultiColumns Plugin
    """
    width = models.CharField(
        _("width"),
        choices=WIDTH_CHOICES,
        default=WIDTH_CHOICES[0][0],
        max_length=50
    )
    cmsplugin_ptr = models.OneToOneField(
        CMSPlugin,
        related_name='%(app_label)s_%(class)s',
        parent_link=True,
        on_delete=models.CASCADE,
    )

    add_class = models.CharField(
        _("class"),
        max_length=50, null=True, blank=True)


    def __str__(self):
        return u"%s" % self.get_width_display()
