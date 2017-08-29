from django import template
register = template.Library()


@register.inclusion_tag('browsing/tags/column_selector.html', takes_context=True)
def column_selector(context):
    try:
        context['togglable_colums']
        return {'columns': context['togglable_colums']}
    except:
        return {'columns': None}
