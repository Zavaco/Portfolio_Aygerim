from django import template
from django.utils.translation import get_language
from ..models import *

register = template.Library()


@register.simple_tag
def get_menus():
    return Menu.objects.all().order_by("order")


@register.simple_tag
def get_footer():
    return Footer.objects.all()


@register.simple_tag
def get_url_tag(request, lang):
    active_language = get_language()
    return request.get_full_path().replace(active_language, lang, 1)
