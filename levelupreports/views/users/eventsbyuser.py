"""Module for generating games by user report"""
from django.shortcuts import render
from django.db import connection
from django.views import View

from levelupreports.views.helpers import dict_fetch_all


class UserEventList(View):
    def get(self, request):
        with connection.cursor() as db_cursor:

            # TODO: Write a query to get all events
            db_cursor.execute("""
            SELECT 
                e.id, 
                e.description, 
                e.date, 
                e.time, 
                u.last_name, 
                u.first_name
            FROM levelupapi_event AS e
            JOIN levelupapi_event_attendees AS a ON a.id = e.gamer_id
            JOIN levelupapi_gamer AS x ON x.id = a.gamer_id
            JOIN auth_user AS u ON u.id = x.user_id
            """)
            # Pass the db_cursor to the dict_fetch_all function to turn the fetch_all() response into a dictionary
            dataset = dict_fetch_all(db_cursor)

            # Take the flat data from the dataset, and build the
            # following data structure for each gamer.
            # This will be the structure of the games_by_user list:
            #
            # [
            #   {
            #     "id": 1,
            #     "full_name": "Admina Straytor",
            #     "games": [
            #       {
            #         "id": 1,
            #         "title": "Foo",
            #         "maker": "Bar Games",
            #         "skill_level": 3,
            #         "number_of_players": 4,
            #         "game_type_id": 2
            #       },
            #       {
            #         "id": 2,
            #         "title": "Foo 2",
            #         "maker": "Bar Games 2",
            #         "skill_level": 3,
            #         "number_of_players": 4,
            #         "game_type_id": 2
            #       }
            #     ]
            #   },
            # ]

            events_by_user = []

            for row in dataset:
                # TODO: Create a dictionary called event that includes 
                # the name, title, number_of_players, maker,
                # event_type_id, and skill_level from the row dictionary
                event = {
                    "id": row["id"],
                    "title": row["title"],
                    "maker": ["maker"],
                    "skill_level": row["skill_level"],
                    "number_of_players": row["number_of_players"],
                    "game_type_id": row["game_type_id"],
                    "user_id": row["user_id"],
                    "full_name": row["first_name"] + "" + row["last_name"]
                
                }
                
                # See if the gamer has been added to the games_by_user list already
                user_dict = None
                for user_event in events_by_user:
                    if user_event['user_id'] == row['user_id']:
                        user_dict = user_event
                
                
                if user_dict:
                    # If the user_dict is already in the events_by_user list, append the event to the events list
                    user_dict['events'].append(event)
                else:
                    # If the user is not on the events_by_user list, create and add the user to the list
                    events_by_user.append({
                        "user_id": row['user_id'],
                        "full_name": row["first_name"] + "" + row["last_name"],
                        "events": [event] 
                    })
        
        # The template string must match the file name of the html template
        template = 'users/list_with_events.html'
        
        # The context will be a dictionary that the template can access to show data
        context = {
            "userevent_list": events_by_user
        }

        return render(request, template, context)
