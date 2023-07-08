from django.db import models

# Create your models here.

class Place(models.Model):
    type = models.CharField(max_length=100, default='CR')
    # CULTURALRICHES = 'CR'
    # FOODANDWINE = 'FW'
    # BIGCITYTHRILLS = 'BT'
    # MOMENTSWATER = 'MW'
    # FRESHAIRNATURE = "FN"
    # BEACHVIBES = 'BV'
    # THEFUTURE = 'TF'
    # TYPE_OF_PLACE_CHOICES = [
    #     (CULTURALRICHES, 'For Cultural Riches'),
    #     (FOODANDWINE, 'For The Food - And Wine'),
    #     (BIGCITYTHRILLS, 'For Big-City Thrills'),
    #     (MOMENTSWATER, 'For Moments On The Water'),
    #     (FRESHAIRNATURE, 'For Fresh Aire And Nature'),
    #     (BEACHVIBES, 'For Beach Vibes'),
    #     (THEFUTURE, 'For A Look At The Future'),
    # ]
    name = models.CharField(max_length=150)
    image = models.CharField(max_length=500)
    bio = models.TextField(max_length=2000)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
