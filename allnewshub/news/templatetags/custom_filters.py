from typing import List
import re
from django import template


register = template.Library()


@register.filter
def first_sentence(value: str) -> str:
    """
    Extracts the first sentence from the given text.
    """
    sentences: List[str] = re.split(r"(?<=[.!?])\s+", value)

    if sentences:
        return sentences[0]
    return value
