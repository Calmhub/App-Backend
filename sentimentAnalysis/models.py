from django.db import models

# Create your models here.

class SentimentRecord(models.Model):
    prediction = models.CharField(max_length = 20)
    date = models.DateField(auto_now_add = True)

def __str__(self):
        return self.prediction