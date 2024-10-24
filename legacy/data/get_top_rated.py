import requests
import json

upcoming_url = "https://api.themoviedb.org/3/movie/upcoming"
popular_url = "https://api.themoviedb.org/3/movie/popular"

def get_movie_data(tmdb_url, jsonFilePath):
  
  tmdb_url = f"https://api.themoviedb.org/3/movie/top_rated?api_key=81e362f4c1140a32fa5dad306fac3a32&language=en-US"
  result = requests.get(tmdb_url).json()
  
  with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(result, indent=4))
  

# jsonFilePath = r"top_rate_tv.json
    

jsonFilePath = r"popular_movie.json" 

get_movie_data(popular_url, jsonFilePath)