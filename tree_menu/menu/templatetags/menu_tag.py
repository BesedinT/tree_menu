from django import template

from ..models import MenuItem

register = template.Library()


@register.simple_tag
def draw_menu(menu_name):
    if menu_name:
        obj = (MenuItem.objects.filter(slug=menu_name)
               .prefetch_related('children'))
    else:
        obj = MenuItem.objects.filter(parent=None).prefetch_related('children')
    return obj
