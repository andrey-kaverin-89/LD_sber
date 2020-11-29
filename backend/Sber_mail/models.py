from django.db import models

class SberMail(models.Model):

    # mail_id = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    # sender = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    subject = models.TextField()
    text = models.TextField()
    short_text = models.TextField()
    tags = models.TextField()
    priority = models.PositiveIntegerField()
    seen = models.BooleanField(default=False)

    # priority = models.PositiveIntegerField()
    # deadline
    # linenos = models.BooleanField(default=False)
    # language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    # style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)


# Create your models here.
