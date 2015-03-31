# coding: utf-8

from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Entry(models.Model):
    from os import path
    
    title = models.CharField(max_length=1024)
    path = models.FilePathField(path=path.join(path.abspath(path.dirname(__file__)), 'templates/entry/entries'), recursive=True)
    post_user = models.CharField(max_length=30)
    post_date_time = models.DateTimeField()
    tags = models.ManyToManyField(Tag)

    def __unicode__(self):
        return self.title
