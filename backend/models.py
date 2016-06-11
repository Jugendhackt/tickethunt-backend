from django.contrib.gis.db import models

# Create your models here.
class TicketTypeAlias(models.Model):
    name = models.CharField(max_length=255, primary_key=True)

class TicketType(models.Model):
    name = models.CharField(max_length=256)
    comment = models.CharField(max_length=500)
    alias = models.ManyToManyField(TicketTypeAlias)

class Ticket(models.Model):
    location = models.PointField()
    ticket_type = models.ManyToManyField(TicketType)
    persons = models.IntegerField()
    comment = models.CharField(max_length=500, blank=True)
    image = models.ImageField(upload_to='./tickets/', null=True)
    valid_until = models.DateTimeField()
