from django import template

register = template.Library()


@register.inclusion_tag("toys/toy_list.html")
def render_toy_list(toys):
    return {
        "toys": toys,
    }


@register.filter
def address(value=""):
    lines = value.split("\n")
    return " ".join(lines)
