from backend.models import Ticket, TicketType, TicketTypeAlias
from rest_framework.serializers import ModelSerializer, ValidationError

import pytz
import datetime

class TicketSerializer(ModelSerializer):
    class Meta:
        model = Ticket
        depth = 1

    def validate_valid_until(self, value):
        """
        Check that the date is at least one second in the future
        """
        now = datetime.datetime.now(pytz.utc)
        if now >= value:
            raise ValidationError("Valid Until must be in the future")
        return value


class TicketTypeAliasSerializer(ModelSerializer):
    class Meta:
        model = TicketTypeAlias


class TicketTypeSerializer(ModelSerializer):
    class Meta:
        model = TicketType
