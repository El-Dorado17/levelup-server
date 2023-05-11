"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Event, Gamer, Game


class EventView(ViewSet):
    """Level up event view"""

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
        event = Event.objects.all()
        serializer = EventSerializer(event, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized event instance
        """
        game = Game.objects.get(pk=request.data["game"])
        # event_type = EventType.objects.get(pk=request.data["event_type"])
        gamer = Gamer.objects.get(user=request.auth.user)

        event = Event.objects.create(
            description=request.data["description"],
            date=request.data["date"],
            time=request.data["time"],
            # attendees=request.data["attendees"],
            game=game,
            gamer=gamer
        )
        serializer = EventSerializer(event)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """Handle PUT requests for a game
        Returns:
            Response -- Empty body with 204 status code
        """
        game = Game.objects.get(pk=request.data["game"])
        gamer = Gamer.objects.get(user=request.auth.user)

        event = Event.objects.get(pk=pk)
        event.description = request.data["description"]
        event.date = request.data["date"]
        event.time = request.data["time"]
        
        event.gamer = gamer
        event.game = game

        #event.gamer = request.data["gamer"]
        #event.attendees = request.data["attendees"]

        #game = Game.objects.get(pk=request.data["game"])
        #gamer = Gamer.objects.get(user=request.auth.user)
        
        event.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)



class EventSerializer(serializers.ModelSerializer):
    """JSON serializer for event     """
    class Meta:
        model = Event
        fields = ('id', 'description', 'date', 'time',
                    'game', 'gamer', 'attendees')
