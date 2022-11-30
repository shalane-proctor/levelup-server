#!/bin/bash
rm -rf levelupapi/migrations
rm db.sqlite3
python3 manage.py migrate
python3 manage.py makemigrations levelupapi
python3 manage.py migrate levelupapi
python3 manage.py loaddata gamers
python3 manage.py loaddata game_types
python3 manage.py loaddata games
python3 manage.py loaddata event
python3 manage.py loaddata event_gamer
