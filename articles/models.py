# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from markdownx.models import MarkdownxField
from taggit.managers import TaggableManager
from django.db import models

# Create your models here.
class Article(models.Model):
	"""
	Description: Model to contain Article
	"""
	title 			= models.CharField(max_length = 200)
	keywords 		= TaggableManager()
	content			= MarkdownxField()
	published_date 	= models.DateTimeField(default=datetime.now)

	class Meta:
		pass