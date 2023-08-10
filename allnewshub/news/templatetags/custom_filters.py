from django import template
import re

register = template.Library()


@register.filter
def first_sentence(value):
    sentences = re.split(r"(?<=[.!?])\s+", value)

    if sentences:
        return sentences[0]
    return value
