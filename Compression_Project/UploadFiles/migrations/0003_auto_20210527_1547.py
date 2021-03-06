# Generated by Django 2.1.7 on 2021-05-27 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UploadFiles', '0002_auto_20210527_1323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inputfile',
            name='Audio',
        ),
        migrations.RemoveField(
            model_name='inputfile',
            name='Video',
        ),
        migrations.RemoveField(
            model_name='outputfile',
            name='Audio',
        ),
        migrations.RemoveField(
            model_name='outputfile',
            name='Video',
        ),
        migrations.AddField(
            model_name='inputfile',
            name='InFile',
            field=models.FileField(blank=True, null=True, upload_to='InFile/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='outputfile',
            name='OutFile',
            field=models.FileField(blank=True, null=True, upload_to='OutFile/%Y/%m/%d'),
        ),
    ]
