from django.template import RequestContext
from django.shortcuts import render_to_response

from thealternativemedicinecabinet.content.models import HealthTip, UpcomingEvent, Media, RecommendedResource

def health_tips(request):
    """Submits the home page information to the URL
    """
    template = "health_tips.html"
    health_tips = HealthTip.objects.all()
    context=locals()
    return render_to_response(template, context, context_instance=RequestContext(request))

def upcoming_events(request):
    """Submits the upcoming event page information to the URL
    """
    template = "upcoming_events.html"
    upcoming_events = UpcomingEvent.objects.all()
    context=locals()
    return render_to_response(template, context, context_instance=RequestContext(request))

def recommended_resources(request):
    """Submits the recommended resources page information to the URL
    """
    template = "recommended_resources.html"
    recommended_resources = RecommendedResource.objects.all()
    context=locals()
    return render_to_response(template, context, context_instance=RequestContext(request))

def media(request):
    """Submits the media page information to the URL
    """
    template = "media.html"
    media_list = Media.objects.all()
    context=locals()
    return render_to_response(template, context, context_instance=RequestContext(request))
