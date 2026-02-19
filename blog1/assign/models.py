from django.db import models

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=100)
    short_desc = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About"

    def __str__(self):
        return self.title


class FollowUs(models.Model):

    PLATFORM_CHOICES = [
        ('github', 'GitHub'),
        ('twitter', 'Twitter'),
        ('linkedin', 'LinkedIn'),
        ('discord', 'Discord'),
    ]

    platform = models.CharField(
        max_length=50,
        choices=PLATFORM_CHOICES
    )

    url = models.URLField()

    def __str__(self):
        return self.get_platform_display()

    class Meta:
        verbose_name = "Follow Us"
        verbose_name_plural = "Follow Us"