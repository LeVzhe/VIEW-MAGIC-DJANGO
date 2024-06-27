from django import template

register = template.Library()

@register.filter(name='split')
def split(value, separator):
    return value.rsplit(separator)[-1]