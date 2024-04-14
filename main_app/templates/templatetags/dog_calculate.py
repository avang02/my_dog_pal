from django import template

register = template.Library()

@register.filter
def dog_calculate(weight):
    return pow(weight, 0.75)

# @register.filter
# def calculate(rounded):
#     return rounded * activity