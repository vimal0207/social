# Generated by Django 3.1 on 2020-12-12 10:17

from django.db import migrations
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_auto_20201211_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='frienddetail',
            name='friendrequestsend',
            field=picklefield.fields.PickledObjectField(default=5, editable=False),
            preserve_default=False,
        ),
    ]