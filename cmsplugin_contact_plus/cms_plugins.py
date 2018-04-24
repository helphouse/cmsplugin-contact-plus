import os.path
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from cmsplugin_contact_plus.admin import ExtraFieldInline
from cmsplugin_contact_plus.exceptions import ResponseRedirectException
from cmsplugin_contact_plus.models import ContactPlus
from cmsplugin_contact_plus.forms import ContactFormPlus


import time


def handle_uploaded_file(f, ts):
    destination = open(os.path.join(settings.MEDIA_ROOT, '{0}-{1}'.format(ts, f.name)), 'wb+')

    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
    
    
class CMSContactPlusPlugin(CMSPluginBase):
    model = ContactPlus
    inlines = [ExtraFieldInline]
    name = _('Contact Form')
    render_template = "cmsplugin_contact_plus/contact.html"
    change_form_template = 'cmsplugin_contact_plus/change_form.html'
    cache = False

    def get_render_template(self, context, instance, placeholder):
        if instance and instance.template:
            return instance.template
        return self.render_template

    def render(self, context, instance, placeholder):
        request = context['request']

        if request.method == "POST" and "contact_plus_form_" + str(instance.id) in request.POST:
            form = ContactFormPlus(
                contactFormInstance=instance,
                request=request,
                data=request.POST,
                files=request.FILES)

            if form.is_valid():
                ts = str(int(time.time()))

                for fl in request.FILES:
                    for f in request.FILES.getlist(fl):
                        handle_uploaded_file(f, ts)

                form.send(instance.recipient_email, request, ts, instance, form.is_multipart)

                raise ResponseRedirectException(redirect(request.get_full_path()))
        else:

            form = ContactFormPlus(
                contactFormInstance=instance,
                request=request)

        context.update({
            'contact': instance,
            'form': form,
        })

        return context


plugin_pool.register_plugin(CMSContactPlusPlugin)
