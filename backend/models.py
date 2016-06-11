from django.contrib.gis.db import models

# Create your models here.
class TicketTypeAlias(models.Model):
    name = models.CharField(max=length=256)
    def __str__(self):
        return self.name

class TicketType(models.Model):
    name = models.CharField(max_length=256)
    comment = models.CharField(max_length=500)
    alias = models.ManyToManyField(TicketTypeAlias)
    area = models.PolygonField()

class Ticket(models.Model):
    location = models.PointField()
    ticket_type = models.ManyToManyField(TicketType)
    persons = models.IntegerField()
    comment = models.CharField(max_length=500)
    image = models.ImageField(upload_to='./tickets/', null=True)
    valid_until = models.DateTimeField()
