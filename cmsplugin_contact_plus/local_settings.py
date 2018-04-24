from django.conf import settings
from django.utils.translation import ugettext_lazy as _

CMSPLUGIN_CONTACT_PLUS_TEMPLATES = getattr(settings, 'CMSPLUGIN_CONTACT_PLUS_TEMPLATES', [
    ('cmsplugin_contact_plus/contact.html', _('Default')),
])



CONTACT_PLUS_EMAIL_TEMPLATES = getattr(settings, 'CONTACT_PLUS_EMAIL_TEMPLATES', {
    'cmsplugin_contact_plus/email.txt': {
        'label': _('Default'),
        'html': 'cmsplugin_contact_plus/email.html'
    }
})
