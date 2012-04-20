from django.forms.models import ModelForm
from django.forms import forms

from thealternativemedicinecabinet.content.models import Email

"""
class InterviewForm(ModelForm):

    class Meta:
        model = Interview

    def save(self, commit=True):
        interview = super(InterviewForm, self).save()
        return interview
"""

class EmailForm(ModelForm):
    """Provides the form for adding emails to the mailing list
    """
    class Meta:
        model = Email

    def save(self, commit=True):
        email = super(EmailForm, self).save()
        return email
