from django.template import RequestContext
from django.shortcuts import render_to_response

from thealternativemedicinecabinet.content.models import HealthTip

def health_tips(request):
    """Submits the home page information to the URL
    """
    template = "health_tips.html"
    health_tips = HealthTip.objects.all()
    context=locals()
    return render_to_response(template, context, context_instance=RequestContext(request))
