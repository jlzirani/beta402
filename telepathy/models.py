# Copyright 2012, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from django.db import models
from users.models import Profile


class Thread(models.Model):
    subject = models.TextField()
    user = models.ForeignKey(Profile)
    referer_id = models.PositiveIntegerField()
    referer_content = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    tags = models.CharField(max_length=100)

    class Meta:
        ordering = ['-created']


class Message(models.Model):
    user = models.ForeignKey(Profile)
    thread = models.ForeignKey(Thread)
    text = models.TextField()
    previous = models.ForeignKey('self', null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, editable=False)
