import random
import string
import csv, json, math
from datetime import datetime, timedelta
from django import template
from django.conf import settings
from django.shortcuts import HttpResponse
from django.utils  import timezone
from django.db.models import Count, Sum, Q

register = template.Library()

@register.filter
def sensor_analytics(null):
    return ""