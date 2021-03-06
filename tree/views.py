# Copyright 2012, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from tree.models import Category
from json import dumps


def get_category(request, id):
    category = get_object_or_404(Category, id=id)
    jsoniser = lambda category: {
        "id": category.id,
         "name": category.name,
         "description": category.description,
         "sub_categories": [{"name": sc.name,
                             "description": sc.description,
                             "id": sc.id} for sc in category.sub_categories.all()],
         "contains": [{"id": cours.id,
                       "name": cours.name,
                       "description": cours.description,
                       "slug": cours.slug} for cours in category.contains.all()]}

    return HttpResponse(dumps(jsoniser(category)), mimetype='application/json')
