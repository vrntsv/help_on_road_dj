from django import template
from django.utils.html import mark_safe
import site_backend.models as models


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


@register.filter
def get_wt_name(wt_id):

    try:
        return models.WorkType.objects.filter(id=wt_id['id_work_type_id']).values('type')[0]['type']
    except TypeError:
        return models.WorkType.objects.filter(id=wt_id).values('type')[0]['type']


@register.filter
def get_city_name(city_id):
    try:
        return models.City.objects.filter(id=city_id).values('city')[0]['city']
    except TypeError:
        return 'err'