from django import template
register = template.Library()
def Swapping(value):
    return value.swapcase()
register.filter('swapping', Swapping)
def Split(value,deliminator):
    return value.split()
register.filter('Split', Split)