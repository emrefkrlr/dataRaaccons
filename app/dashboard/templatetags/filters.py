import re
from vendor.math import math_functions
from django import template



register = template.Library()

@register.filter(name='custom_index')
def custom_index(indexable, i):
    if i > 11:
        i = 0
    return indexable[i]

@register.filter
def remove_substr(string, char):
    for s in string:
        r = s.replace(char, '')
        return r


@register.filter
def change_of_rate(main, general):

    ratio = math_functions.rate_of_change(last=main, now=general)
    
    return ratio


@register.filter
def rate(main, p2):

    rate = math_functions.rate(p1=main, p2=p2)
    
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


