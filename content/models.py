from django.db import models


class Email(models.Model):
    """ Model for the emails submitted to be added to the mailing list
    """
    email = models.EmailField()

    def __unicode__(self):
        return self.email

class HealthTip(models.Model):
    """ the logic for the admin-editable health tips 
    """
    title = models.CharField(max_length=255)
    date = models.DateField()
    tip = models.TextField()

    class Meta:
        ordering = ['-date']
        get_latest_by = "date"

    def __unicode__(self):
        return self.title

class UpcomingEvent(models.Model):
    """ the logic for the admin-editable upcoming events
    """
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    link = models.CharField(max_length=255, blank=True)
    date_and_time = models.DateTimeField()
    description = models.TextField()

    class Meta:
        ordering = ['-date_and_time']
        get_latest_by = "date_and_time"

    def __unicode__(self):
        return self.title

class YoutubeVideo(models.Model):
    """ the logic for the video template tag
    """
    video_id = models.CharField(max_length=255)
    date = models.DateField()

    class Meta:
        ordering = ['-date']
        get_latest_by = "date"

    def __unicode__(self):
        return str(self.date)

class RecommendedResource(models.Model):
    """ the logic for the admin-editable recommended resources 
    """
    title = models.CharField(max_length=255)
    site = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()

    class Meta:
        ordering = ['-date']
        get_latest_by = "date"

    def __unicode__(self):
        return self.title

MEDIA_OPTIONS = (
    ('W', 'Written'),
    ('R', 'Radio'),
    ('T', 'Television'),
)

class Media(models.Model):
    """ the logic for the admin-editable media page 
    """
    title = models.CharField(max_length=255, blank=True)
    link = models.CharField(max_length=255, blank=True)
    date = models.DateField()
    description = models.TextField(blank=True)
    category = models.CharField(max_length=2,choices=MEDIA_OPTIONS,default='W', blank=True)
    class Meta:
        ordering = ['-date']
        get_latest_by = "date"

    def __unicode__(self):
        return self.title


class Review(models.Model):
    description = models.TextField()
    source = models.CharField(max_length = 255)
    date = models.DateField()

    class Meta:
        ordering = ['-date']
        get_latest_by = "date"

    def __unicode__(self):
        return self.source

class SpeakingReview(models.Model):
    description = models.TextField()
    source = models.CharField(max_length = 255)
    date = models.DateField()

    class Meta:
        ordering = ['-date']
        get_latest_by = "date"

    def __unicode__(self):
        return self.source

class ConsultText(models.Model):
    header = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateField()

    class Meta:
        ordering = ['-date']
        get_latest_by = "date"

    def __unicode__(self):
        return str(self.date)

