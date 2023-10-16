from django import template

register = template.Library()

CURRENCIES_SIMBOLS = {
    'rub': '₽',
    'usd': '$'
}

@register.filter()

def currency(value, code='rub'):
    """
    :param value: значение, к которому нужно применить фильтр
    """
    postfix = CURRENCIES_SIMBOLS[code]
    return f'{value} {postfix}'





