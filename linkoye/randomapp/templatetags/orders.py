# in your app's templatetags/groupby.py file
from itertools import groupby

from django import template

register = template.Library()

@register.filter
def groupby_attr(items, attr):
    return groupby(sorted(items, key=lambda x: getattr(x, attr)), key=lambda x: getattr(x, attr))
