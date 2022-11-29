from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Gamer


class GamerView(ViewSet):
    """Level up Gamer view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single Gamer
        Returns:
            Response -- JSON serialized Gamer
        """

        try:
            gamer = Gamer.objects.get(pk=pk)
            serializer = GamerSerializer(gamer)
            return Response(serializer.data)
        except Gamer.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all Gamers
        Returns:
            Response -- JSON serialized list of Gamers
        """
        gamers = Gamer.objects.all()
        serializer = GamerSerializer(gamers, many=True)
        return Response(serializer.data)


class GamerSerializer(serializers.ModelSerializer):
    """JSON serializer for Gamers
    """
    class Meta:
        model = Gamer
        fields = ('uid', 'bio')
