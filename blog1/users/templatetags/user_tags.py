# What this does:
# Takes a user object and a group_name string.
# Returns True if the user is in that group.

from django import template

register = template.Library()

@register.filter(name='in_group')
def in_group(user, group_name):
    """Return True if the user is in the given group."""
    return user.groups.filter(name=group_name).exists()