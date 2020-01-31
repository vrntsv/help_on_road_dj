from django import template
from django.utils.html import mark_safe


register = template.Library()

@register.filter
def multiply(value, arg):
    return value * arg

@register.filter
def count_percent(value, percent):
    return value * percent / 100

@register.filter
def count_user_percent(value, percent):
    percent = 100 - percent
    return value * percent / 100
