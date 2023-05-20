from typing import Dict

from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()


@register.filter
def get_item(dict: Dict[str, int], key: int) -> int:
    """Фильтр получения значения элемента словаря по ключу"""

    return dict.get(str(key))
