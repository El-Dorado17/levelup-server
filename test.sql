
/*
All Games
Gamer first name, last name, id
*/

-- SELECT 
--     g.title,
--     g.number_of_players,
--     g.skill_level,
--     g.game_type_id,
--     x.user_id,
--     u.first_name,
--     u.last_name,
--     x.id
-- FROM levelupapi_game AS g
-- JOIN levelupapi_gamer AS x ON x.id = g.gamer_id
-- JOIN auth_user AS u ON u.id = x.user_id 

-- SELECT * FROM levelupapi_game
-- SELECT * FROM levelupapi_gamer
-- SELECT * FROM auth_user

-- SELECT 
--     g.title,
--     g.number_of_players,
--     g.skill_level,
--     g.game_type,
--     x.user,
--     x.id
-- FROM Game AS g
-- JOIN Gamer AS x ON x.id = Game.gamer




-- Chapt 4
--event each user is going to

SELECT e.id, e.description, e.date, e.time, u.last_name, u.first_name
FROM levelupapi_event AS e
JOIN levelupapi_event_attendees AS a ON a.id = e.gamer_id
JOIN levelupapi_gamer AS x ON x.id = a.gamer_id
JOIN auth_user AS u ON u.id = x.user_id 





SELECT *
FROM levelupapi_event_attendees AS a
JOIN levelupapi_gamer AS x ON x.id = a.gamer_id
JOIN auth_user AS u ON u.id = x.user_id 