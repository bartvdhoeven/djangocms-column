# Generated by Django 2.2.16 on 2020-09-10 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_column', '0002_auto_20160915_0818'),
    ]

    operations = [
        migrations.AddField(
            model_name='multicolumns',
            name='add_class',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='class'),
        ),
    ]