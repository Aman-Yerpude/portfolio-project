# Generated by Django 2.0.2 on 2019-02-04 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='title',
            field=models.CharField(default=1, max_length=32),
            preserve_default=False,
        ),
    ]
