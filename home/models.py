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
    Description = models.TextField(max_length=500, default='Please describe the welfare case here & select the condition of the horse below:')
    Condition = models.IntegerField(choices=RATING_SCALE, default=1)


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    conf_num = models.CharField(max_length=15)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.email + " (" + ("not " if not self.confirmed else "") + "confirmed)"