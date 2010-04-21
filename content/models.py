from django.db import models

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
