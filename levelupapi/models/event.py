from django.db import models

class Event(models.Model):

    description = models.CharField(max_length=60)
    date = models.DateField()
    time = models.TimeField()
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    attendees = models.ManyToManyField("Gamer",related_name="attending")

#Why are foreignkeys in quotes? 
#? it allows for a connection without need for import
