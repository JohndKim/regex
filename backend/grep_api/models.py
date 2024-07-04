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
        return f'string: {self.string}, regex: {self.regex}'

class uploaded_image(models.Model):
    img = models.ImageField(blank=True, null=True)
    
    def __str__(self):
        return f'image: smth'