import json
from cinemarsapp import db
from cinemarsapp.models import DVD, Genre, Actor
from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base

file_path = './cinemarsapp/static/data/data.json'

gen_path = './cinemarsapp/static/data/genres.json'
act_path = './cinemarsapp/static/data/actors.json.json'

series_path = './cinemarsapp/static/data/series.json'
new_path = './cinemarsapp/static/data/data.json'

with open(new_path) as file:
    data = json.load(file)
    
with open(gen_path) as genres_file:
    genres_data = json.load(genres_file)
    
with open(act_path) as actor_file:
    actors_data = json.load(actor_file)
    
for dvd_data in data:
  
  dvd = DVD(
    title = dvd_data['title'],
    original_title = dvd_data['original_title'],
    adult=dvd_data['adult'],
    description=dvd_data['overview'],
    background_image=dvd_data['backdrop_path'],
    poster_image=dvd_data['poster_path'],
    release_date=datetime.strptime(dvd_data['release_date'], "%Y-%m-%d"),
    rating=dvd_data['vote_average'],
    price=dvd_data['price'],
    runningtime=dvd_data['runtime'],
    episode = dvd_data['episode']
  )
  db.session.add(dvd)

for genre_d in genres_data:
    genre = Genre(
        id = genre_d['id'],
        name = genre_d['name']
    )
    db.session.add(genre)
    
for actor_d in actors_data:
    actor = Actor(
        id = actor_d['id'],
        name = actor_d['name']
    )
    db.session.add(actor)

db.session.commit()