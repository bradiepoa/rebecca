# Generated by Django 3.1.2 on 2022-04-25 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gettreat', '0005_auto_20220425_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='our_doctors',
            name='status',
            field=models.CharField(blank=True, choices=[('permanent', 'Permanent'), ('temperory', 'Temperory'), ('not available', 'Not available')], default='temperory', max_length=200, null=True),
        ),
    ]