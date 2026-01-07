from django.db import models

# Create your models here.

class AboutModel(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About"

    def __str__(self):
        return self.title
    
class SocialLinks(models.Model):
    platform = models.CharField(max_length=100)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Social Link"
        verbose_name_plural = "Social Links"

    def __str__(self):
        return self.platform