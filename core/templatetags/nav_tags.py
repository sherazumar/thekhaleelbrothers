from django import template
register = template.Library()


@register.simple_tag(takes_context=True)
def nav_active(context, url_name):
    from django.urls import reverse, NoReverseMatch
    try:
        path = reverse(url_name)
    except NoReverseMatch:
        path = url_name
    if context['request'].path == path:
        return "active"  # This class name can be whatever you choose
    return ""
