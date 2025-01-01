from django import template
register = template.Library()


@register.filter(name = 'remove_special_char')
def remove_character(value, arg):
    for characters in arg:
        value = value.replace(characters, '')
    return value
    