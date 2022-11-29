from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import EventGamer


class EventGamerView(ViewSet):
    """Level up Event view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single event
        Returns:
            Response -- JSON serialized event
        """
        event_gamer = EventGamer.objects.get(pk=pk)
        serializer = EventSerializer(event_gamer)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all events
        Returns:
            Response -- JSON serialized list of events
        """
        event_gamers = EventGamer.objects.all()
        gamer_id = request.query_params.get('gamer_id', None)
        if gamer_id is not None:
            event_gamers = event_gamers.filter(gamer_id=gamer_id)
        event_id = request.query_params.get('event_id', None)
        if event_id is not None:
            event_gamers = event_gamers.filter(event_id=event_id)
        serializer = EventSerializer(event_gamers, many=True)
        return Response(serializer.data)


class EventSerializer(serializers.ModelSerializer):
    """JSON serializer for events
    """
    class Meta:
        model = EventGamer
        fields = ('gamer', 'event')
        depth = 2
