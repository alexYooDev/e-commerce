import json
from flask import Blueprint
from . import db
from .models import DVD, Genre, Actor
from datetime import datetime
import traceback

bp = Blueprint('admin', __name__, url_prefix="/admin/")

@bp.route("/dbseed/")
def dbseed():
  gen_path = './cinemarsapp/static/data/genres.json'
  act_path = './cinemarsapp/static/data/actors.json'
  new_path = './cinemarsapp/static/data/data.json'

  with open(new_path) as file:
      data = json.load(file)
      
  with open(gen_path) as genres_file:
      genres_data = json.load(genres_file)
      
  with open(act_path) as actor_file:
      actors_data = json.load(actor_file)
  
  try:
    for dvd_data in data:
      
      dvd = DVD(
        title = dvd_data['title'],
        original_title = dvd_data['original_title'],
        adult=dvd_data['adult'],
        description=dvd_data['overview'],
        category=dvd_data['category'],
        background_image=dvd_data['backdrop_path'],
        poster_image=dvd_data['poster_path'],
        release_date=datetime.strptime(dvd_data['release_date'], "%Y-%m-%d"),
        rating=dvd_data['vote_average'],
        price=dvd_data['price'],
        runtime=dvd_data['runtime'],
        episodes=dvd_data['episodes']
      )
      
      db.session.add(dvd)
      
  except Exception as e:
    traceback.print_exc()
    return "There was an issue adding the dvds in dbseed function"  
  try:
    for genre_d in genres_data:
        genre = Genre(
            id = genre_d['id'],
            name = genre_d['name']
        )
        db.session.add(genre)
  except:
    return "There was an issue adding the genres in dbseed function"  
  try:   
    for actor_d in actors_data:
        actor = Actor(
            id = actor_d['id'],
            name = actor_d['name']
        )
        db.session.add(actor)
  except:
    return "There was an issue adding the actors in dbseed function"
  
  try:
    db.session.commit()
  except:
    traceback.print_exc()
    return "There was an issue adding data into DB"
  
  return "DATA Filled"