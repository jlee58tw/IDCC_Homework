from django import template
from concert.models import Subscribe

register = template.Library()

@register.filter
def getsub(value,subscribes):

	flag = 0
	for subscribe in subscribes:
		if int(subscribe.singerid) == int(value):
			flag = 1

 	return flag