from django.db import models


class Contact(models.Model):
    """
    Class Contact model that creates and saves the comment in the DB
    """
    RATING_SCALE = (

        (1, 'Poor condition'),
        (2, 'Thin'),
        (3, 'Moderate'),
        (4, 'Fleshy'),
        (5, 'Fat'),

    )

    County = models.CharField(max_length=50, default='')
    Town = models.CharField(max_length=50, default='')
    Eircode = models.CharField(max_length=10, default='')
    Description = models.TextField(max_length=100, default='Please describe the welfare case here & select the condition of the horse below:')
    Condition = models.IntegerField(choices=RATING_SCALE, default=1)
    