from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Event, Gamer, Game

class EventSerializer(serializers.ModelSerializer):
    """JSON serializer for events
    """
    class Meta:
        model = Event
        fields = ('id', 'game', 'description', 'date', 'time', 'organizer')
        depth = 2
class EventView(ViewSet):
    """Level up Event view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single event
        Returns:
            Response -- JSON serialized event
        """
        event = Event.objects.get(pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all events
        Returns:
            Response -- JSON serialized list of events
        """
        events = Event.objects.all()
        game = request.query_params.get('game', None)
        if game is not None:
            events = events.filter(game_id=game)
        organizer = request.query_params.get('organizer', None)
        if organizer is not None:
            events = events.filter(gamer_id=organizer)
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def create(self, request):
        
        organizer = Gamer.objects.get(pk=request.data["organizer"])
        game = Game.objects.get(pk=request.data["game"])

        event = Event.objects.create(
            description=request.data["description"],
            date=request.data["date"],
            time=request.data["time"],
            organizer=organizer,
            game=game
        )
        serializer = EventSerializer(event)
        return Response(serializer.data)
