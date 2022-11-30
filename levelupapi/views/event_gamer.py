from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import EventGamer, Gamer, Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventGamer
        fields = ('gamer', 'event')
        depth = 2
class EventGamerView(ViewSet):

    def retrieve(self, request, pk):
        event_gamer = EventGamer.objects.get(pk=pk)
        serializer = EventSerializer(event_gamer)
        return Response(serializer.data)

    def list(self, request):

        event_gamers = EventGamer.objects.all()
        gamer_id = request.query_params.get('gamer_id', None)
        if gamer_id is not None:
            event_gamers = event_gamers.filter(gamer_id=gamer_id)
        event_id = request.query_params.get('event_id', None)
        if event_id is not None:
            event_gamers = event_gamers.filter(event_id=event_id)
        serializer = EventSerializer(event_gamers, many=True)
        return Response(serializer.data)

    def create(self, request):

        gamer = Gamer.objects.get(pk=request.data["gamer"])
        event = Event.objects.get(pk=request.data["event"])

        event_gamer = EventGamer.objects.create(
            gamer=gamer,
            event=event,
        )
        serializer = EventSerializer(event_gamer)
        return Response(serializer.data)
