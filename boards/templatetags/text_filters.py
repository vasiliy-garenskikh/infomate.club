import re

from django import template
from django.utils.html import urlize
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def pretty_url(value):
    return re.sub(r"https?://(www\.)?", "", value, 1)


@register.filter
def cool_number(value, num_decimals=1):
    """
    Django template filter to convert regular numbers to a cool format (ie: 2K, 434.4K, 33M...)
    """
    int_value = int(value)
    formatted_number = '{{:.{}f}}'.format(num_decimals)
    if int_value < 1000:
        return str(int_value)
    elif int_value < 1000000:
        return formatted_number.format(int_value / 1000.0).rstrip('0.') + 'K'
    else:
        return formatted_number.format(int_value / 1000000.0).rstrip('0.') + 'M'


@register.filter
def smart_urlize(value, target="_blank"):
    # TODO: this
    return mark_safe(urlize(value))


@register.filter
def rupluralize(value, arg="дурак,дурака,дураков"):
    args = arg.split(",")
    number = abs(int(value))
    a = number % 10
    b = number % 100

    if (a == 1) and (b != 11):
        return args[0]
    elif (a >= 2) and (a <= 4) and ((b < 10) or (b >= 20)):
        return args[1]
    else:
        return args[2]
