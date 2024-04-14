from django import template

register = template.Library()

@register.simple_tag
def dog_calculate(weight, activity):
    return pow(weight, 0.75)*activity

# @register.filter
# def calculate(rounded):
#     return rounded * activity