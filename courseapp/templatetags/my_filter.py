from django import template

register = template.Library()


@register.filter(name='ordering')
def ordering(content, param='date_add'):
    data = content.order_by(param)
    return data
