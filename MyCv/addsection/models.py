from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Addsection(models.Model):


    class Summary(models.Model):
        summary_text = models.CharField(max_length=200)
        last_modified_date = models.DateTimeField('date modified')
        def __str__(self):
            return  self.summary_text

    class JobTitle(models.Model):
        jobtitle_text = models.CharField(max_length=200)
        last_modified_date = models.DateTimeField('date modified')
        date_start = models.DateTimeField
        date_end = models.DateTimeField
        def __str__(self):
            return  self.jobtitle_text
        def was_published_recently(self):
            return self.last_modified_date >= timezone.now() - datetime.timedelta(days=1)



