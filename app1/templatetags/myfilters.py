from django import template

register = template.Library()

@register.filter
def mymodulo(num, val):
    print("num = %s,val = %s\n" % (num,val))
    return num % val == 0
