import re
from vendor.math import math_functions
from django import template



register = template.Library()

@register.filter(name='custom_index')
def custom_index(indexable, i):
    if i > 14:
        i = 0
    return indexable[i]

@register.filter
def remove_substr(string, char):
    for s in string:
        r = s.replace(char, '')
        return r


@register.filter
def change_of_rate(current, previous):

    print("Current", current)
    print("Previous", previous)

    ratio = math_functions.rate_of_change(current=current, previous=previous)
    
    return ratio


@register.filter
def rate(divisor, base):

    rate = math_functions.rate(divisor=divisor, base=base)
    
    return rate


@register.filter
def timeline_data(main):

    result = []

    for d in main:
        
        result.append({
            "company": d["company_name"],
            "price": d["total_avg_price"],
            "logo": d["company_logo"],
            "columnSettings": { 
                        "fill": "am5.color(KTUtil.getCssVariableValue('--bs-primary'))"
                    }
        })
        
    return result


@register.filter(name='replace_and_capitalize')
def replace_and_capitalize(p1):
    
    return p1.replace("_", " ").capitalize()


