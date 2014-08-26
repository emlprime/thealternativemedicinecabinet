from django import template

from thealternativemedicinecabinet.content.models import UpcomingEvent

register = template.Library()

@register.filter

@register.inclusion_tag("upcoming_events.html")
def display_events():
    return {"events": UpcomingEvent.objects.all()}
