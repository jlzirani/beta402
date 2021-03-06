# Copyright 2012, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from django.db import models
from users.models import Profile
from tree.models import Course


class Document(models.Model):
    name = models.TextField()
    description = models.TextField()
    user = models.ForeignKey(Profile)
    reference = models.ForeignKey(Course)

    size = models.PositiveIntegerField(null=True, default=0)
    words = models.PositiveIntegerField(null=True, default=0)
    pages = models.PositiveIntegerField(null=True, default=0)
    date = models.DateTimeField(auto_now=True)

    view = models.PositiveIntegerField(null=True, default=0)
    download = models.PositiveIntegerField(null=True, default=0)


class Page(models.Model):
    document = models.ForeignKey(Document)
    numero = models.IntegerField()
    height_120 = models.IntegerField()
    height_600 = models.IntegerField()
    height_900 = models.IntegerField()


class PendingDocument(models.Model):
    document = models.ForeignKey(Document)
    state = models.CharField(max_length=30)
    url = models.CharField(max_length=255)
    done = models.PositiveIntegerField(default=0)
