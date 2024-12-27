from django import template
register = template.Library()


@register.filter(name = 'remove_special_char')

def remove_character(value, arg):
    print("Values : ",value)
    print("Args : ",arg)
    for characters in arg:
        print("Character ",characters)
        value = value.replace(characters, '')
    return value
    