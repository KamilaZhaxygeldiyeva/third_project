from django import template
from poll.models import *
register = template.Library()

@register.simple_tag()
def get_types():
    return Types.objects.all()