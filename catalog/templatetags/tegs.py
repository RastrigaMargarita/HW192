import datetime
from django import template

register = template.Library()

# Создание тега
@register.simple_tag()
def mediapath(image_path):
    return "/media/" + str(image_path)


