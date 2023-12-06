from django import template
from django.utils.safestring import mark_safe
from bleach import clean

register = template.Library()

ALLOWED_TAGS = {"a", "i", "strong", "code"}


@register.filter
def allow_specific_tags(value):
    cleaned_value = clean(value, tags=ALLOWED_TAGS, attributes={})
    return mark_safe(cleaned_value)
