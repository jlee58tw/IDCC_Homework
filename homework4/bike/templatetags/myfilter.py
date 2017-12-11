from django import template

register = template.Library()

@register.filter
def divideToPercent(value, arg): 
	return int(float(value) / float(arg) *100)