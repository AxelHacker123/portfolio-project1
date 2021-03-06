from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255, default = '')
    pub_date = models.DateTimeField(blank=True, null=True)
    body = models.TextField(default='')
    image = models.ImageField(upload_to='images/', default="")
