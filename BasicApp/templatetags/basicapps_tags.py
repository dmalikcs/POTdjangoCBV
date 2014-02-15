from django import template

register = template.Library()

@register.inclusion_tag('results.html',takes_context=True)
def name(context):
    print context
    return {'name':'Deepak Malik'}
