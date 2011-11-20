from django import template

from thealternativemedicinecabinet.content.models import YoutubeVideo

register = template.Library()

@register.filter

@register.inclusion_tag("youtube_video.html")
def display_video():
    return {"youtube_video": YoutubeVideo.objects.latest()}
