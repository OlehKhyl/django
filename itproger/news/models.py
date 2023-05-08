from django.db import models

# Create your models here.

class Articles(models.Model):
    title = models.CharField('Title', max_length=50)
    anouns = models.CharField('Anouns', max_length=250)
    full_text = models.TextField('News text')
    date = models.DateTimeField('Publish date')

    def get_absolute_url(self):
        return f'/news/{self.id}'

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
