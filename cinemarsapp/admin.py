import json
from flask import Blueprint
from . import db
from .models import DVD, Genre, Actor
from datetime import datetime
import traceback

bp = Blueprint('admin', __name__, url_prefix="/admin/")

@bp.route("/dbseed/")
def dbseed():
  genre_dict= {}
  actor_dict = {}
  
  gen_path = './cinemarsapp/static/data/genres.json'
  act_path = './cinemarsapp/static/data/actors.json'
  new_path = './cinemarsapp/static/data/data.json'  
  
  with open(new_path) as file:
    dvds = json.load(file)
      
  with open(gen_path) as genres_file:
    genres = json.load(genres_file)
    
  with open(act_path) as actor_file:
    actors = json.load(actor_file)
    
  
  try:
    for genre in genres:
        genre_obj = Genre(
            id = genre['id'],
            name = genre['name']
        )
        db.session.add(genre_obj)
        genre_dict[genre['name']] = genre_obj
    
  except:
    traceback.print_exc()
    return "There was an issue adding the genres in dbseed function"  
  try:   
    for actor in actors:
        actor_obj = Actor(
            id = actor['id'],
            name = actor['name']
        )
        db.session.add(actor_obj)
        actor_dict[actor['name']] = actor_obj
    
  except:
    traceback.print_exc()
    return "There was an issue adding the actors in dbseed function"
  
  try:
    for dvd in dvds:
      
      dvd_obj = DVD(
        id = dvd['id'],
        title = dvd['title'],
        original_title = dvd['original_title'],
        adult=dvd['adult'],
        description=dvd['overview'],
        category=dvd['category'],
        director=dvd['director'],
        background_image=dvd['backdrop_path'],
        poster_image=dvd['poster_path'],
        release_date=datetime.strptime(dvd['release_date'], "%Y-%m-%d"),
        rating=dvd['vote_average'],
        price=dvd['price'],
        running_time=dvd['runtime'],
        episodes=dvd['episodes']
      )
      
      for genre_name in dvd['genres']:
        genre_obj = genre_dict.get(genre_name)
        if genre_obj:
          dvd_obj.genres.append(genre_obj)
          
      for actor_name in dvd['main_actors']:
        actor_obj = actor_dict.get(actor_name)
        if actor_obj:
          dvd_obj.actors.append(actor_obj)
        
      db.session.add(dvd_obj)
  except:
    traceback.print_exc()
    return "There was an issue adding the dvds in dbseed function"  
  
  try:
    db.session.commit()
  except:
    traceback.print_exc()
    return "There was an issue adding data into DB"
  
  return "DATA Filled"
