import re
from django import template
from django.urls import reverse, NoReverseMatch

register = template.Library()


@register.simple_tag(takes_context=True)
def active(context, name):
    try:
        pattern = reverse(name)
    except NoReverseMatch:
        return ""
    if re.match(pattern, context["request"].path_info):
        return "active"
    return ""
