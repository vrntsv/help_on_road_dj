from django import template
from django.utils.html import mark_safe
import site_backend.models as models


register = template.Library()

@register.filter
def multiply(value, arg):
    return value * arg


@register.filter
def count_percent(value, percent):
    try:
        return value * percent / 100
    except:
        return 'err'

@register.filter('get_amm_with_city')
def get_amm_with_city(dict_data, key):
    """
    usage example {{ your_dict|get_value_from_dict:your_key }}
    """
    print(dict_data, key)
    return dict_data, key

@register.filter
def pass_wt(_dict_id_city, _id_wt):
    _dict, _id_city = _dict_id_city
    print('_dict', _dict )
    print('_id_city', _id_city )
    for value in _dict:
        print('value ', value)
        if value['id_city'] == _id_city and value['id'] == _id_wt:
            print('true')
            return value['COUNT(employees.id)']
    return None


@register.filter
def count_user_percent(value, percent):
    try:
        user_percent = 100 - percent
        return value * user_percent / 100
    except:
        return 'err'

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
    except Exception:
        return 'err'


@register.filter
def do_abs(number):
    try:
        return abs(number)
    except TypeError:
        return number