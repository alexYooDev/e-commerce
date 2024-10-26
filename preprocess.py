import json
from datetime import datetime
import random

file_path = './cinemarsapp/static/data/data.json'

gen_path = './cinemarsapp/static/data/genres.json'
act_path = './cinemarsapp/static/data/genres.json'

series_path = './cinemarsapp/static/data/series.json'
new_path = './cinemarsapp/static/data/data.json'

with open(new_path) as file:
    data = json.load(file)

revised_data = []
    
for dvd_data in data:
  if 'price' not in dvd_data:
    dvd_data['price'] = round(random.uniform(10.1,15.9),2)
    
  if 'runtime' not in dvd_data:
    dvd_data['runtime'] = 0
  
  revised_data.append(dvd_data)

  if 'episodes' not in dvd_data:
    dvd_data['episodes'] = 0
    
  if 'director' not in dvd_data:
    dvd_data['director'] = 'Anonymous'
  
  if 'main_actors' not in dvd_data:
    dvd_data['main_actors'] = []
# with open(file_path, 'r') as movies_file:
#   movies = json.load(movies_file)

# with open(series_path, 'r') as series_file:
#   series = json.load(series_file)
  
# revised_data = []

# for movie in movies:
#   revised_data.append(movie)

# for s in series:
#   revised_data.append(s)
  
with open(new_path, 'w') as new_file:
  json.dump(revised_data, new_file, indent=4)

# with open(file_path, 'r') as file:
#     data = json.load(file)

# unique_genres = {}
# unique_actors = {}

# genre_mapping = {
#     "Drama": 18,
#     "Crime": 80,
#     "Fantasy": 14,
#     "Comedy": 35,
#     "Thriller": 53,
#     "Romance": 10749,
#     "War": 10752,
#     "Animation": 16,
#     "Family": 10751,
#     "Action": 28,
#     "Biography": 36,
#     "History": 36,
#     "Western": 37,
# }

# for dvd_data in data:
#   for genre_name in dvd_data["genres"]:
#     if genre_name not in unique_genres:
#       unique_genres[genre_name] = {
#         "id": genre_mapping.get(genre_name, None),
#         "name": genre_name
#       }
#   for actor_name in dvd_data['main_actors']:
#     if actor_name not in unique_actors:
#       unique_actors[actor_name] = {
#         "id": len(unique_actors) + 1,
#         "name": actor_name
#       }  
      
# genres_list = list(unique_genres.values())
# actors_list = list(unique_actors.values())

# with open(act_path, 'w') as actors_file:
#   json.dump(actors_list, actors_file, indent=4)
  
  
  