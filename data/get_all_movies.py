import pandas as pd
import requests
import sys
from tqdm import tqdm
import time 
import random

def add_url(row):
  return f"http://www.imdb.com/title/tt{row}"

def add_details(df):
  for i, row in tqdm(df.iterrows(), total=df.shape[0]):
    tmdb_id = row['tmdbId']
    tmdb_url = f"https://api.themoviedb.org/3/movie/{tmdb_id}?api_key=81e362f4c1140a32fa5dad306fac3a32&language=en-US"
    
    result = requests.get(tmdb_url)
    
    # final url : https://image.tmdb.org/t/p/original/
    try:
      df.at[i, "poster_path"] = "https://image.tmdb.org/t/p/original" + result.json()['poster_path']
      df.at[i, "backdrop_path"] = "https://image.tmdb.org/t/p/original" + result.json()['backdrop_path']
      df.at[i, "overview"] = result.json()['overview']
      df.at[i, "runtime"] = result.json()['runtime']
      df.at[i, "summary"] = result.json()['tagline']
      df.at[i, "release_date"] = result.json()['release_date']
      df.at[i, "rating"] = result.json()['vote_average']
      
      price = random.random() * 10
      df.at[i, "price"] = price
    
      time.sleep(0.1)
      
    except(TypeError, KeyError) as e:
      
      # toy story poster as default
      df.at[i, 'poster_path'] = 'https://image.tmdb.org/t/p/original/uXDfjJbdP4ijw5hWSBrPrIKpxab.jpg' 
      
  return df

if __name__ == "__main__":
  
  movies_df = pd.read_csv('movies.csv')
  
  # id를 문자로 인식하도록 type 변경
  movies_df['movieId'] = movies_df['movieId'].astype(str)
  link_df = pd.read_csv('links.csv', dtype=str)
  merged_df = movies_df.merge(link_df, on='movieId', how='left')
  merged_df['url'] = merged_df['imdbId'].apply(lambda x: add_url(x))
  result_df = merged_df
  result_df["summary"] = None
  result_df["overview"] = None
  result_df["runtime"] = None
  result_df["rating"] = None
  result_df["release_date"] = None
  result_df['poster_path'] = None
  result_df["backdrop_path"] = None
  result_df = add_details(result_df)
  result_df.to_csv('movies_final.csv', index=None)