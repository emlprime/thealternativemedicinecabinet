from django.template import RequestContext
from django.shortcuts import render_to_response

from thealternativemedicinecabinet.content.models import HealthTip, UpcomingEvent, Media, RecommendedResource, Email, Review, SpeakingReview, ConsultText
from thealternativemedicinecabinet.content.forms import EmailForm

def consult(request):
    """ Submits Consult Text to the URL
    """
    template="consult.html"
    consult_text = ConsultText.objects.latest()
    context=locals()
    return render_to_response(template, context, context_instance=RequestContext(request))

def speaking(request):
    """ Submits Speaking Reviews to the URL
    """
    template="speaking.html"
    reviews = SpeakingReview.objects.all()
    context=locals()
    return render_to_response(template, context, context_instance=RequestContext(request))

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
    review_list = Review.objects.all()
    email_form=EmailForm()
    context=locals()
    return render_to_response(template, context, context_instance=RequestContext(request))

def email_add(request):
    """ Creates an email object and notifies Kathy that she has a new email subscriber
    """
    if request.method=='POST':
        print "request method is post"
        page = request.META['HTTP_REFERER'] if request.META.has_key('HTTP_REFERER') else '/'
        values = request.POST.copy()
        print values
        form=EmailForm(values)
        if form.is_valid():
            print "form is valid"
            email=form.save()
            message = "%s has subscribed to your email mailing list" % (email)
            #try to send mail. If it fails, print an error
            try:
                send_mail('Email Subscriber to Healing Circle', message, 'subscribers@healingcirclemassage.com', ['healingcirclemassage@hotmail.com'], fail_silently=False)
            except:
                print "Error: could not send mail"
        else:
            print "form is not valid", form.errors
            errors = form.errors
    context=locals()
    return HttpResponseRedirect(page)
