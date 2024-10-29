# import json
# from datetime import datetime
# import random
import hashlib


# file_path = './cinemarsapp/static/data/data.json'

# gen_path = './cinemarsapp/static/data/genres.json'
# act_path = './cinemarsapp/static/data/genres.json'

# series_path = './cinemarsapp/static/data/series.json'
# new_path = './cinemarsapp/static/data/data.json'

# with open(new_path) as file:
#     data = json.load(file)

# revised_data = []
    
# for dvd_data in data:
#   if 'price' not in dvd_data:
#     dvd_data['price'] = round(random.uniform(10.1,15.9),2)
    
#   if 'runtime' not in dvd_data:
#     dvd_data['runtime'] = 0
  
#   revised_data.append(dvd_data)

#   if 'episodes' not in dvd_data:
#     dvd_data['episodes'] = 0
    
#   if 'director' not in dvd_data:
#     dvd_data['director'] = 'Anonymous'
  
#   if 'main_actors' not in dvd_data:
#     dvd_data['main_actors'] = []
# # with open(file_path, 'r') as movies_file:
# #   movies = json.load(movies_file)

# # with open(series_path, 'r') as series_file:
# #   series = json.load(series_file)
  
# # revised_data = []

# # for movie in movies:
# #   revised_data.append(movie)

# # for s in series:
# #   revised_data.append(s)
  
# with open(new_path, 'w') as new_file:
#   json.dump(revised_data, new_file, indent=4)

# # with open(file_path, 'r') as file:
# #     data = json.load(file)

# # unique_genres = {}
# # unique_actors = {}

# # genre_mapping = {
# #     "Drama": 18,
# #     "Crime": 80,
# #     "Fantasy": 14,
# #     "Comedy": 35,
# #     "Thriller": 53,
# #     "Romance": 10749,
# #     "War": 10752,
# #     "Animation": 16,
# #     "Family": 10751,
# #     "Action": 28,
# #     "Biography": 36,
# #     "History": 36,
# #     "Western": 37,
# # }

# # for dvd_data in data:
# #   for genre_name in dvd_data["genres"]:
# #     if genre_name not in unique_genres:
# #       unique_genres[genre_name] = {
# #         "id": genre_mapping.get(genre_name, None),
# #         "name": genre_name
# #       }
# #   for actor_name in dvd_data['main_actors']:
# #     if actor_name not in unique_actors:
# #       unique_actors[actor_name] = {
# #         "id": len(unique_actors) + 1,
# #         "name": actor_name
# #       }  
      
# # genres_list = list(unique_genres.values())
# # actors_list = list(unique_actors.values())

# # with open(act_path, 'w') as actors_file:
# #   json.dump(actors_list, actors_file, indent=4)
  
  
  
import json
import requests

# Replace with your TMDB API key
API_KEY = "81e362f4c1140a32fa5dad306fac3a32"
BASE_URL = "https://api.themoviedb.org/3"

# Load the dataset
with open('./cinemarsapp/static/data/data.json', 'r') as file:
    data = json.load(file)

# def get_tv_id(title):
#     """Fetches the TV ID for a given title."""
#     search_url = f"{BASE_URL}/search/tv"
#     params = {"api_key": API_KEY, "query": title}
#     response = requests.get(search_url, params=params)
#     results = response.json().get('results')
#     if results:
#         return results[0].get('id')
#     return None

# def get_series_details(tv_id):
#     """Fetches director, main actors, and number of episodes for a given TV ID."""
#     # Retrieve credits (for director and main actors)
#     credits_url = f"{BASE_URL}/tv/{tv_id}/credits"
#     params = {"api_key": API_KEY}
#     credits_response = requests.get(credits_url, params=params)
#     credits = credits_response.json()

#     # Extract director(s) from crew
#     director = next((member["name"] for member in credits.get("crew", []) if member["job"] == "Director"), "Director Unknown")
    
#     # Extract main actors from cast (limiting to top 5)
#     main_actors = [member["name"] for member in credits.get("cast", [])[:5]]
#     if not main_actors:
#         main_actors = ["Cast Unknown"]

#     # Retrieve series details (for episode count)
#     details_url = f"{BASE_URL}/tv/{tv_id}"
#     details_response = requests.get(details_url, params=params)
#     details = details_response.json()
#     episode_count = details.get("number_of_episodes", 0)

#     return director, main_actors, episode_count

# # Update series entries with director, main actors, and episode count
# for item in data:
#     if item["category"] == "series" and (not item.get("director") or not item.get("main_actors") or item.get("episodes") == 0):
#         tv_id = get_tv_id(item["title"])
#         if tv_id:
#             director, main_actors, episode_count = get_series_details(tv_id)
#             item["director"] = director
#             item["main_actors"] = main_actors
#             item["episodes"] = episode_count

# # Save updated data to a new file
# with open('updated_data_with_real_cast_and_episodes.json', 'w') as file:
#     json.dump(data, file, indent=4)

# print("Data updated with real cast, crew, and episode count information.")

def generate_actor_id(name):
    return hashlib.md5(name.encode()).hexdigest()[:8]  # Shorten the hash to 8 characters for readability

actors_dict = {}

# Extract actors from each series
for item in data:
    id = 1
    if item["category"] == "series" and item.get("main_actors"):
        for actor in item["main_actors"]:
            actor_id = id 
            id = id + 1
            if actor_id not in actors_dict:
                actors_dict[actor_id] = {"id": actor_id, "name": actor}

# Convert the dictionary to a list for JSON output
actors_list = list(actors_dict.values())

# Save the actors data to a new JSON file
with open('actors.json', 'w') as file:
    json.dump(actors_list, file, indent=4)

print("Actors data extracted to actors.json.")