# Generated by Django 3.1.2 on 2022-04-14 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gettreat', '0003_auto_20220415_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bills',
            name='status',
            field=models.CharField(blank=True, choices=[('pending', 'Pending'), ('cleared', 'Cleared')], default='pending', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='our_patients',
            name='gender',
            field=models.CharField(blank=True, choices=[('female', 'Female'), ('male', 'Male')], default='female', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='our_patients',
            name='status',
            field=models.CharField(blank=True, choices=[('on hold', 'On Hold'), ('admitted', 'Admitted'), ('discharged', 'Discharged')], default='on hold', max_length=200, null=True),
        ),
    ]
