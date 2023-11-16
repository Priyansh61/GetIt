from django.db import models

# Create your models here.

event_type_choices = [
    ('virtual','Virtual'),
    ('physical','Physical'),
]   
class Event (models.Model) :
    title = models.CharField(max_length=200)
    organizer_id = models.OneToOneField(
        'accounts.Account',
        on_delete=models.CASCADE,
        default=None,
        null=True,
        blank=True,
    )
    description = models.TextField(max_length=600,
                                      blank=True)
    email = models.EmailField(max_length=254,
                                blank=True)
    phone = models.CharField(max_length=15, blank=True)
    date = models.DateField(
        blank = False,
        null = False,
    )
    time = models.TimeField(
        blank = False,
        null = False,
    )
    event_type = models.CharField(max_length=100,
                                  choices=event_type_choices)

    location = models.CharField(max_length=200)
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title