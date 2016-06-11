from django.contrib.gis.db import models

# Create your models here.
class TicketTypeAlias(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    def __str__(self):
        return self.name

class TicketType(models.Model):
    comment = models.CharField(max_length=500)
    show_name = models.ForeignKey(TicketTypeAlias, related_name='%(class)s_show')
    names = models.ManyToManyField(TicketTypeAlias)#, related_name='%(class)s_requests_created')
    def __str__(self):
        return self.show_name

class Ticket(models.Model):
    location = models.PointField()
    ticket_type = models.ManyToManyField(TicketType)
    persons = models.IntegerField()
    comment = models.CharField(max_length=500, blank=True)
    image = models.ImageField(upload_to='./tickets/', null=True)
    valid_until = models.DateTimeField()
