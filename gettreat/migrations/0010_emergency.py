# Generated by Django 3.1.2 on 2022-04-22 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gettreat', '0009_auto_20220415_0335'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emergency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_Name', models.CharField(blank=True, max_length=200, null=True)),
                ('Phone_Number', models.CharField(blank=True, max_length=15, null=True)),
                ('patient_id', models.CharField(blank=True, max_length=100, null=True)),
                ('Location_Discription', models.TextField(blank=True, null=True)),
                ('Request_Date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(blank=True, choices=[('declined', 'Declined'), ('pending', 'Pending'), ('picked', 'Picked')], max_length=200)),
                ('location', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='gettreat.location')),
            ],
        ),
    ]
