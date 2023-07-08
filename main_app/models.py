from django.db import models

# Create your models here.

CATEGORY_CHOICES_ABBREV = (
    ('For Cultural Riches', 'CR'),
    ('For the Food - And Wine', 'FW'),
    ('For Big-city Thrills', 'BT'),
    ('For Moments On The Water', 'MW'),
    ('For Fresh Air and Nature', 'FN'),
    ('For Beach Vibes', 'BV'),
    ('For A Look At The Future', 'TF'),
)

CATEGORY_CHOICES_FULL = (
    ('For Cultural Riches', 'For Cultural Riches'),
    ('For the Food - And Wine', 'For the Food - And Wine'),
    ('For Big-city Thrills', 'For Big-city Thrills'),
    ('For Moments On The Water', 'For Moments On The Water'),
    ('For Fresh Air and Nature', 'For Fresh Air and Nature'),
    ('For Beach Vibes', 'For Beach Vibes'),
    ('For A Look At The Future', 'For A Look At The Future'),
)

class Place(models.Model):
    type = models.CharField(max_length=25, choices=CATEGORY_CHOICES_ABBREV, default='-')
    typefull = models.CharField(max_length=50, choices=CATEGORY_CHOICES_FULL, default='-')
    name = models.CharField(max_length=150)
    image = models.CharField(max_length=500)
    bio = models.TextField(max_length=2000)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
