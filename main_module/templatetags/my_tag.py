from django import template

register = template.Library()

@register.filter
def get_parent_color(obj):
    try:
        c=obj.get_parent_color()
    except :
        c="#FFFFFF"
    return c
