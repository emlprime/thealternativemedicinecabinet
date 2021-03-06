import urllib
import urllib2
import json

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

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
        page = request.META['HTTP_REFERER'] if request.META.has_key('HTTP_REFERER') else '/'
        values = request.POST.copy()
        form=EmailForm(values)
        if form.is_valid():
            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.urlencode(values)
            req = urllib2.Request(url, data)
            response = urllib2.urlopen(req)
            result = json.load(response)
            ''' End reCAPTCHA validation '''

            if result['success']:
                email=form.save()
                message = "%s has subscribed to your email mailing list" % (email)
                try:
                    send_mail('Email Subscriber to from thealternativemedicinecabinet.com', message, 'subscribers@healingcirclemassage.com', ['drkathygruver@gmail.com'], fail_silently=False)
                except:
                    send_mail('Problem with Email Subscriber to Healing Circle', "there is something wrong with the email server" , 'subscribers@healingcirclemassage.com', ['laura@emlprime.com'], fail_silently=False)
            else:
                send_mail('Problem with Email Subscriber to Healing Circle', "recaptcha fail" , 'subscribers@healingcirclemassage.com', ['laura@emlprime.com'], fail_silently=False)
        else:
            errors = form.errors
    else:
        page = request.META['HTTP_REFERER'] if request.META.has_key('HTTP_REFERER') else '/'
    context=locals()
    return HttpResponseRedirect(page)
