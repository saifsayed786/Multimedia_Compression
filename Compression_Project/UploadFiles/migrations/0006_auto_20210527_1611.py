# Generated by Django 2.1.7 on 2021-05-27 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UploadFiles', '0005_auto_20210527_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputfile',
            name='File',
            field=models.FileField(blank=True, null=True, upload_to='File/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='outputfile',
            name='OutFile',
            field=models.FileField(blank=True, null=True, upload_to='File/%Y/%m/%d'),
        ),
    ]
