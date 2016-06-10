from django.contrib.gis.db import models

# Create your models here.
class TicketType(models.Model):
    name = models.CharField(max_length=256)
    def __str__(self):
        return self.name

class Ticket(models.Model):
    location = models.PointField()
    ticket_type = models.ManyToManyField(TicketType)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='./tickets/', null=True)
    valid_until = models.DateTimeField()