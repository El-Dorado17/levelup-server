
/*
All Games
Gamer first name, last name, id
*/

SELECT 
    g.title,
    g.number_of_players,
    g.skill_level,
    g.game_type_id,
    x.user_id,
    x.id FROM levelupapi_game AS g
JOIN levelupapi_gamer AS x
JOIN auth_user AS u ON u.id = x.user_id 

SELECT * FROM levelupapi_game
SELECT * FROM levelupapi_gamer

-- SELECT 
--     g.title,
--     g.number_of_players,
--     g.skill_level,
--     g.game_type,
--     x.user,
--     x.id
-- FROM Game AS g
-- JOIN Gamer AS x ON x.id = Game.gamer