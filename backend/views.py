from backend.models import Ticket, TicketType
from backend.serializers import TicketSerializer, TicketTypeSerializer
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework_gis.filters import InBBoxFilter
from rest_framework_extensions.mixins import CacheResponseAndETAGMixin

class DefaultViewSet(CacheResponseAndETAGMixin, viewsets.ModelViewSet):
    model_class = None
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        assert self.model_class is not None, "You need to override model_class"
        queryset = self.model_class.objects.all()
        return queryset

    def get_serializer_class(self):
        assert self.model_class is not None, "You need to override model_class"
        serializer_name = "%sSerializer" % self.model_class.__name__
        return globals()[serializer_name]

class TicketViewSet(DefaultViewSet):
    model_class = Ticket
    bbox_filter_field = 'location'
    filter_backends = (InBBoxFilter, )

class TicketTypeViewSet(DefaultViewSet):
    model_class = TicketType