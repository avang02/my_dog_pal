from django import template

register = template.Library()

@register.simple_tag
def kcal_day(weight, activity):
    return pow(weight, 0.75) * activity