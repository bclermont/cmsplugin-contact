# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='form_layout',
            field=models.CharField(help_text='Choice the layout of contact form', max_length=255, verbose_name='Form Layout', choices=[(b'dashcare_website.contact_form.forms.CustomContactForm', b'Custom')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='site_email',
            field=models.EmailField(max_length=254, verbose_name='Email recipient'),
        ),
    ]
