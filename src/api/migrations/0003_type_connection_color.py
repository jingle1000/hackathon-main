# Generated by Django 2.1.7 on 2019-02-23 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_profileconnection'),
    ]

    operations = [
        migrations.AddField(
            model_name='type',
            name='connection_color',
            field=models.CharField(default='#fff', max_length=20),
        ),
    ]
