from django.db import models
from django.db.models.signals import post_save
from pathlib import Path
import subprocess
import os
import ffmpeg
from django.dispatch import receiver
from celery.task import task
# Create your models here.
class Files(models.Model):
    
    InFile =  models.FileField(upload_to='assets/Input_Files',null=True, blank=True)
    OutFile =  models.FileField(upload_to='assets/OutPut_Files',null=True, blank=True,editable=True)

    # def __str__(self):
    #     return self.InFile
from django.dispatch.dispatcher import Signal
def reducer(self):
    return (Signal, (self.providing_args,))
Signal.__reduce__ = reducer

@task(ignore_result=True)
def files_after_save(sender, instance, **kwargs):
    Output_file = instance.InFile.path
    from django.db import connection

    with connection.cursor() as cursor:
        cursor.execute("UPDATE `uploadfiles_files` SET `OutFile` = `InFile` WHERE `id` = %s",instance.id)
    split_tup = os.path.splitext(Output_file)
    file_name = split_tup[0]
    file_extension = split_tup[1]
    # print("File Name: ", file_name)
    # print("File Extension: ", file_extension)
    video_ext_list = ['.mp4','.webm','.flv','.avi','.mkv','.mov']
    audio_ext_list = ['.wav','.aac','.mp3']
    image_ext_list = ['.png',',gif','.tiff','.jpg']
    
    video_ext = '.mp4'
    audio_ext = '.mp3'
    image_ext = '.jpg'
    
    Out = "\\".join(Output_file.split('\\')[:-2])
    dirs = Out+ "\\" +'Output_Files'
    a = (Path(Output_file).stem)
    
    Path(dirs).mkdir(exist_ok=True)
    # ---------------------Video----------------------------
    if file_extension in video_ext_list:
        output = dirs+"\\"+a+video_ext
        # output = file_name+video_ext
        cmd = "ffmpeg -i " + Output_file.replace(" ","/") + " -c:v libx264 -preset veryslow -crf 35 "+ output.replace(" ","/")
        subprocess.run(cmd)
        # Files.objects.filter(id=instance.pk).update(OutFile=file_name+video_ext)
        Files.objects.filter(id=instance.pk).update(OutFile=output)
    # ---------------------Audio----------------------------
    elif file_extension in audio_ext_list:
        output = dirs+"\\"+a+audio_ext
        cmd = "ffmpeg -i " + Output_file.replace(" ","/") + " -vn -c:a libmp3lame -b:a 224K -ac 2 "+ output.replace(" ","/")
        subprocess.run(cmd)
        # Files.objects.filter(id=instance.pk).update(OutFile=file_name+audio_ext)
        Files.objects.filter(id=instance.pk).update(OutFile=output)
    # ---------------------Image----------------------------
    elif file_extension in image_ext_list:
        output = dirs+"\\"+a+image_ext
        cmd = "ffmpeg -i " + Output_file.replace(" ","/") + " -preset veryslow "+ output.replace(" ","/")
        subprocess.run(cmd)
        # Files.objects.filter(id=instance.pk).update(OutFile=file_name+image_ext)
        Files.objects.filter(id=instance.pk).update(OutFile=output)

post_save.connect(files_after_save.delay,sender=Files)