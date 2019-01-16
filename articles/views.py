# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Article
from django.shortcuts import render

# Create your views here.
def index(request):
	article = Article.objects.first()
	context = { 'article': article }
	return render(request, 'index.html', context)