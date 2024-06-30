from django.db import models

# Create your models here.

class grep_pair(models.Model):
    '''
    string: string
    regex: regex pattern
    '''
    string = models.CharField(max_length=100)
    regex = models.CharField(max_length=100)

    def __str__(self):
        return 'image'