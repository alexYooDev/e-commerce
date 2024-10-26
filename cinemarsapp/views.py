from flask import Blueprint, render_template
from .models import DVD,Genre,Actor, dvd_genre_association, dvd_actor_association
from . import db
import traceback

bp = Blueprint('main', __name__)

#  MOCK_DATA
# movies = [
#     {
#       "adult": False,
#       "backdrop_path": "/kXfqcdQKsToO0OUXHcrrNCHDBzO.jpg",
#       "genre_ids": [18, 80],
#       "id": 278,
#       "original_language": "en",
#       "original_title": "The Shawshank Redemption",
#       "overview": "Imprisoned in the 1940s for the double murder of his wife and her lover, upstanding banker Andy Dufresne begins a new life at the Shawshank prison, where he puts his accounting skills to work for an amoral warden. During his long stretch in prison, Dufresne comes to be admired by the other inmates -- including an older prisoner named Red -- for his integrity and unquenchable sense of hope.",
#       "poster_path": "/9cqNxx0GxF0bflZmeSMuL5tnGzr.jpg",
#       "release_date": "1994-09-23",
#       "title": "The Shawshank Redemption",
#       "director": "Frank Darabont",
#       "main_actors": [
#         "Tim Robbins",
#         "Morgan Freeman",
#         "Bob Gunton",
#         "William Sadler",
#         "Clancy Brown"
#       ],
#       "genres": ["Drama", "Crime"],
#       "runtime": 142,
#       "rating": 8.707,
#       "price": 9.99
#     },
#     {
#       "adult": False,
#       "backdrop_path": "/tmU7GeKVybMWFButWEGl2M4GeiP.jpg",
#       "genre_ids": [18, 80],
#       "id": 238,
#       "original_language": "en",
#       "original_title": "The Godfather",
#       "overview": "Spanning the years 1945 to 1955, a chronicle of the fictional Italian-American Corleone crime family. When organized crime family patriarch, Vito Corleone barely survives an attempt on his life, his youngest son, Michael steps in to take care of the would-be killers, launching a campaign of bloody revenge.",
#       "poster_path": "/3bhkrj58Vtu7enYsRolD1fZdja1.jpg",
#       "release_date": "1972-03-14",
#       "title": "The Godfather",
#       "director": "Francis Ford Coppola",
#       "main_actors": [
#         "Marlon Brando",
#         "Al Pacino",
#         "James Caan",
#         "Robert Duvall",
#         "Diane Keaton"
#       ],
#       "genres": ["Crime", "Drama"],
#       "runtime": 175,
      
#       "rating": 8.69,
#       "price": 11.99
#     },
#     {
#       "adult": False,
#       "backdrop_path": "/kGzFbGhp99zva6oZODW5atUtnqi.jpg",
#       "genre_ids": [18, 80],
#       "id": 240,
#       "original_language": "en",
#       "original_title": "The Godfather Part II",
#       "overview": "In the continuing saga of the Corleone crime family, a young Vito Corleone grows up in Sicily and in 1910s New York. In the 1950s, Michael Corleone attempts to expand the family business into Las Vegas, Hollywood and Cuba.",
#       "poster_path": "/hek3koDUyRQk7FIhPXsa6mT2Zc3.jpg",
#       "release_date": "1974-12-20",
#       "title": "The Godfather Part II",
#       "director": "Francis Ford Coppola",
#       "main_actors": [
#         "Al Pacino",
#         "Robert De Niro",
#         "Robert Duvall",
#         "Diane Keaton",
#         "John Cazale"
#       ],
#       "genres": ["Crime", "Drama"],
#       "runtime": 202,
#       "rating": 8.575,
#       "price": 10.99
#     },
#     {
#       "adult": False,
#       "backdrop_path": "/zb6fM1CX41D9rF9hdgclu0peUmy.jpg",
#       "genre_ids": [18, 36, 10752],
#       "id": 424,
#       "original_language": "en",
#       "original_title": "Schindler's List",
#       "overview": "The true story of how businessman Oskar Schindler saved over a thousand Jewish lives from the Nazis while they worked as slaves in his factory during World War II.",
#       "poster_path": "/sF1U4EUQS8YHUYjNl3pMGNIQyr0.jpg",
#       "release_date": "1993-12-15",
#       "title": "Schindler's List",
#       "director": "Steven Spielberg",
#       "main_actors": [
#         "Liam Neeson",
#         "Ben Kingsley",
#         "Ralph Fiennes",
#         "Caroline Goodall",
#         "Jonathan Sagall"
#       ],
#       "genres": ["Biography", "Drama", "History", "War"],
#       "runtime": 195,
#       "rating": 8.565,
#       "price": 8.99
#     },
#     {
#       "adult": False,
#       "backdrop_path": "/qqHQsStV6exghCM7zbObuYBiYxw.jpg",
#       "genre_ids": [18],
#       "id": 389,
#       "original_language": "en",
#       "original_title": "12 Angry Men",
#       "overview": "The defense and the prosecution have rested and the jury is filing into the jury room to decide if a young Spanish-American is guilty or innocent of murdering his father. What begins as an open and shut case soon becomes a mini-drama of each of the jurors' prejudices and preconceptions about the trial, the accused, and each other.",
#       "poster_path": "/ow3wq89wM8qd5X7hWKxiRfsFf9C.jpg",
#       "release_date": "1957-04-10",
#       "title": "12 Angry Men",
#       "director": "Sidney Lumet",
#       "main_actors": [
#         "Henry Fonda",
#         "Lee J. Cobb",
#         "Martin Balsam",
#         "Jack Warden",
#         "E.G. Marshall"
#       ],
#       "genres": ["Drama"],
#       "runtime": 96,
      
#       "rating": 8.546,
#       "price": 7.99
#     },
#     {
#       "adult": False,
#       "backdrop_path": "/6oaL4DP75yABrd5EbC4H2zq5ghc.jpg",
#       "genre_ids": [16, 10751, 14],
#       "id": 129,
#       "original_language": "ja",
#       "original_title": "\u5343\u3068\u5343\u5c0b\u306e\u795e\u96a0\u3057",
#       "overview": "A young girl, Chihiro, becomes trapped in a strange new world of spirits. When her parents undergo a mysterious transformation, she must call upon the courage she never knew she had to free her family.",
#       "poster_path": "/39wmItIWsg5sZMyRUHLkWBcuVCM.jpg",
#       "release_date": "2001-07-20",
#       "title": "Spirited Away",
#       "director": "Hayao Miyazaki",
#       "main_actors": [
#         "Rumi Hiiragi",
#         "Miyu Irino",
#         "Mari Natsuki",
#         "Takeshi Naito",
#         "Yasuko Sawaguchi"
#       ],
#       "genres": ["Animation", "Family", "Fantasy"],
#       "runtime": 125,
      
#       "rating": 8.537,
#       "price": 9.99
#     },
#     {
#       "adult": False,
#       "backdrop_path": "/90ez6ArvpO8bvpyIngBuwXOqJm5.jpg",
#       "genre_ids": [35, 18, 10749],
#       "id": 19404,
#       "original_language": "hi",
#       "original_title": "\u0926\u093f\u0932\u0935\u093e\u0932\u0947 \u0926\u0941\u0932\u094d\u0939\u0928\u093f\u092f\u093e \u0932\u0947 \u091c\u093e\u092f\u0947\u0902\u0917\u0947",
#       "overview": "Raj is a rich, carefree, happy-go-lucky second generation NRI. Simran is the daughter of Chaudhary Baldev Singh, who in spite of being an NRI is very strict about adherence to Indian values. Simran has left for India to be married to her childhood fianc\u00e9. Raj leaves for India with a mission at his hands, to claim his lady love under the noses of her whole family. Thus begins a saga.",
#       "poster_path": "/lfRkUr7DYdHldAqi3PwdQGBRBPM.jpg",
#       "release_date": "1995-10-20",
#       "title": "Dilwale Dulhania Le Jayenge",
#       "director": "Aditya Chopra",
#       "main_actors": [
#         "Shah Rukh Khan",
#         "Kajol",
#         "Amrish Puri",
#         "Farida Jalal",
#         "Anupam Kher"
#       ],
#       "genres": ["Comedy", "Drama", "Romance"],
#       "runtime": 190,
#       "rating": 8.529,
#       "price": 11.99
#     },
#     {
#       "adult": False,
#       "backdrop_path": "/nMKdUUepR0i5zn0y1T4CsSB5chy.jpg",
#       "genre_ids": [18, 28, 80, 53],
#       "id": 155,
#       "original_language": "en",
#       "original_title": "The Dark Knight",
#       "overview": "Batman raises the stakes in his war on crime. With the help of Lt. Jim Gordon and District Attorney Harvey Dent, Batman sets out to dismantle the remaining criminal organizations that plague the streets. The partnership proves to be effective, but they soon find themselves prey to a reign of chaos unleashed by a rising criminal mastermind known to the terrified citizens of Gotham as the Joker.",
#       "poster_path": "/qJ2tW6WMUDux911r6m7haRef0WH.jpg",
#       "release_date": "2008-07-16",
#       "title": "The Dark Knight",
#       "director": "Christopher Nolan",
#       "main_actors": [
#         "Christian Bale",
#         "Heath Ledger",
#         "Aaron Eckhart",
#         "Michael Caine",
#         "Maggie Gyllenhaal"
#       ],
#       "genres": ["Action", "Crime", "Drama", "Thriller"],
#       "runtime": 152,
#       "rating": 8.515,
#       "price": 10.99
#     },
#     {
#       "adult": False,
#       "backdrop_path": "/8eihUxjQsJ7WvGySkVMC0EwbPAD.jpg",
#       "genre_ids": [35, 53, 18],
#       "id": 496243,
#       "original_language": "ko",
#       "original_title": "\uae30\uc0dd\ucda9",
#       "overview": "All unemployed, Ki-taek's family takes peculiar interest in the wealthy and glamorous Parks for their livelihood until they get entangled in an unexpected incident.",
#       "poster_path": "/7IiTTgloJzvGI1TAYymCfbfl3vT.jpg",
#       "release_date": "2019-05-30",
#       "title": "Parasite",
#       "director": "Bong Joon-ho",
#       "main_actors": [
#         "Song Kang-ho",
#         "Lee Sun-kyun",
#         "Cho Yeo-jeong",
#         "Choi Woo-shik",
#         "Park So-dam"
#       ],
#       "genres": ["Comedy", "Drama", "Thriller"],
#       "runtime": 132,
#       "rating": 8.506,
#       "price": 8.99
#     },
#     {
#       "adult": False,
#       "backdrop_path": "/vxJ08SvwomfKbpboCWynC3uqUg4.jpg",
#       "genre_ids": [14, 18, 80],
#       "id": 497,
#       "original_language": "en",
#       "original_title": "The Green Mile",
#       "overview": "A supernatural tale set on death row in a Southern prison, where gentle giant John Coffey possesses the mysterious power to heal people's ailments. When the cell block's head guard, Paul Edgecomb, recognizes Coffey's miraculous gift, he tries desperately to help stave off the condemned man's execution.",
#       "poster_path": "/8VG8fDNiy50H4FedGwdSVUPoaJe.jpg",
#       "release_date": "1999-12-10",
#       "title": "The Green Mile",
#       "director": "Frank Darabont",
#       "main_actors": [
#         "Tom Hanks",
#         "Michael Clarke Duncan",
#         "David Morse",
#         "Bonnie Hunt",
#         "James Cromwell"
#       ],
#       "genres": ["Crime", "Drama", "Fantasy"],
#       "runtime": 189,
#       "rating": 8.5,
#       "price": 7.99
#     },
#     {
#       "adult": False,
#       "backdrop_path": "/suaEOtk1N1sgg2MTM7oZd2cfVp3.jpg",
#       "genre_ids": [53, 80],
#       "id": 680,
#       "original_language": "en",
#       "original_title": "Pulp Fiction",
#       "overview": "A burger-loving hit man, his philosophical partner, a drug-addled gangster's moll and a washed-up boxer converge in this sprawling, comedic crime caper. Their adventures unfurl in three stories that ingeniously trip back and forth in time.",
#       "poster_path": "/d5iIlFn5s0ImszYzBPb8JPIfbXD.jpg",
#       "release_date": "1994-09-10",
#       "title": "Pulp Fiction",
      
#       "rating": 8.5,
#       "price": 9.99,
#       "director": "James Cameron",
#       "main_actors": [
#         "Sam Worthington",
#         "Zoe Saldana",
#         "Sigourney Weaver",
#         "Stephen Lang",
#         "Giovanni Ribisi"
#       ],
#       "genres": ["Action", "Adventure", "Sci-Fi"],
#       "runtime": 162
#     },
#     {
#       "adult": False,
#       "backdrop_path": "/dIWwZW7dJJtqC6CgWzYkNVKIUm8.jpg",
#       "genre_ids": [16, 10749, 18],
#       "id": 372058,
#       "original_language": "ja",
#       "original_title": "\u541b\u306e\u540d\u306f\u3002",
#       "overview": "High schoolers Mitsuha and Taki are complete strangers living separate lives. But one night, they suddenly switch places. Mitsuha wakes up in Taki\u2019s body, and he in hers. This bizarre occurrence continues to happen randomly, and the two must adjust their lives around each other.",
#       "poster_path": "/vfJFJPepRKapMd5G2ro7klIRysq.jpg",
#       "release_date": "2016-08-26",
#       "title": "Your Name.",
#       "rating": 8.486,
#       "price": 11.99,
#       "director": "Makoto Shinkai",
#       "main_actors": [
#         "Ryunosuke Kamiki",
#         "Mone Kamishiraishi",
#         "Ryo Narita",
#         "Aoi Yuki",
#         "Nobunaga Shimazaki"
#       ],
#       "genres": ["Animation", "Romance", "Drama"],
#       "runtime": 106
#     },
#     {
#       "adult": False,
#       "backdrop_path": "/2u7zbn8EudG6kLlBzUYqP8RyFU4.jpg",
#       "genre_ids": [12, 14, 28],
#       "id": 122,
#       "original_language": "en",
#       "original_title": "The Lord of the Rings: The Return of the King",
#       "overview": "As armies mass for a final battle that will decide the fate of the world--and powerful, ancient forces of Light and Dark compete to determine the outcome--one member of the Fellowship of the Ring is revealed as the noble heir to the throne of the Kings of Men. Yet, the sole hope for triumph over evil lies with a brave hobbit, Frodo, who, accompanied by his loyal friend Sam and the hideous, wretched Gollum, ventures deep into the very dark heart of Mordor on his seemingly impossible quest to destroy the Ring of Power.\u200b",
#       "poster_path": "/rCzpDGLbOoPwLjy3OAm5NUPOTrC.jpg",
#       "release_date": "2003-12-17",
#       "title": "The Lord of the Rings: The Return of the King",
#       "rating": 8.482,
#       "price": 10.99,
#       "director": "Peter Jackson",
#       "main_actors": [
#         "Elijah Wood",
#         "Ian McKellen",
#         "Viggo Mortensen",
#         "Orlando Bloom",
#         "Sean Astin"
#       ],
#       "genres": ["Action", "Adventure", "Drama", "Fantasy"],
#       "runtime": 201
#     },
#     {
#       "adult": False,
#       "backdrop_path": "/ghgfzbEV7kbpbi1O8eIILKVXEA8.jpg",
#       "genre_ids": [35, 18, 10749],
#       "id": 13,
#       "original_language": "en",
#       "original_title": "Forrest Gump",
#       "overview": "A man with a low IQ has accomplished great things in his life and been present during significant historic events\u2014in each case, far exceeding what anyone imagined he could do. But despite all he has achieved, his one true love eludes him.",
#       "poster_path": "/arw2vcBveWOVZr6pxd9XTd1TdQa.jpg",
#       "release_date": "1994-06-23",
#       "title": "Forrest Gump",
#       "rating": 8.472,
#       "price": 8.99,
#       "director": "Robert Zemeckis",
#       "main_actors": [
#         "Tom Hanks",
#         "Robin Wright",
#         "Gary Sinise",
#         "Mykelti Williamson",
#         "Sally Field"
#       ],
#       "genres": ["Drama", "Romance"],
#       "runtime": 142
#     },
#     {
#       "adult": False,
#       "backdrop_path": "/7TF4p86ZafnxFuNqWdhpHXFO244.jpg",
#       "genre_ids": [18, 80],
#       "id": 769,
#       "original_language": "en",
#       "original_title": "GoodFellas",
#       "overview": "The true story of Henry Hill, a half-Irish, half-Sicilian Brooklyn kid who is adopted by neighbourhood gangsters at an early age and climbs the ranks of a Mafia family under the guidance of Jimmy Conway.",
#       "poster_path": "/aKuFiU82s5ISJpGZp7YkIr3kCUd.jpg",
#       "release_date": "1990-09-12",
#       "title": "GoodFellas",
#       "rating": 8.5,
#       "price": 7.99,
#       "director": "Martin Scorsese",
#       "main_actors": [
#         "Robert De Niro",
#         "Ray Liotta",
#         "Joe Pesci",
#         "Lorraine Bracco",
#         "Paul Sorvino"
#       ],
#       "genres": ["Crime", "Drama"],
#       "runtime": 162
#     },
#     {
#       "adult": False,
#       "backdrop_path": "/Adrip2Jqzw56KeuV2nAxucKMNXA.jpg",
#       "genre_ids": [37],
#       "id": 429,
#       "original_language": "it",
#       "original_title": "Il buono, il brutto, il cattivo",
#       "overview": "While the Civil War rages on between the Union and the Confederacy, three men \u2013 a quiet loner, a ruthless hitman, and a Mexican bandit \u2013 comb the American Southwest in search of a strongbox containing $200,000 in stolen gold.",
#       "poster_path": "/bX2xnavhMYjWDoZp1VM6VnU1xwe.jpg",
#       "release_date": "1966-12-22",
#       "title": "The Good, the Bad and the Ugly",
#       "rating": 8.462,
#       "price": 9.99,
#       "director": "Sergio Leone",
#       "main_actors": [
#         "Clint Eastwood",
#         "Lee Van Cleef",
#         "Eli Wallach",
#         "Aldo Giuffre",
#         "Luigi Pistilli"
#       ],
#       "genres": ["Western"],
#       "runtime": 178
#     },
#     {
#       "adult": False,
#       "backdrop_path": "/sJNNMCc6B7KZIY3LH3JMYJJNH5j.jpg",
#       "genre_ids": [28, 18],
#       "id": 346,
#       "original_language": "ja",
#       "original_title": "\u4e03\u4eba\u306e\u4f8d",
#       "overview": "A samurai answers a village's request for protection after he falls on hard times. The town needs protection from bandits, so the samurai gathers six others to help him teach the people how to defend themselves, and the villagers provide the soldiers with food.",
#       "poster_path": "/8OKmBV5BUFzmozIC3pPWKHy17kx.jpg",
#       "release_date": "1954-04-26",
#       "title": "Seven Samurai",
#       "rating": 8.5,
#       "price": 11.99,
#       "director": "Akira Kurosawa",
#       "main_actors": [
#         "Toshiro Mifune",
#         "Takashi Shimura",
#         "Keiko Tsushima",
#         "Yoshio Inaba",
#         "Seiji Miyaguchi"
#       ],
#       "genres": ["Action", "Drama"],
#       "runtime": 207
#     },
#     {
#       "adult": False,
#       "backdrop_path": "/gwj4R8Uy1GwejKqfofREKI9Jh7L.jpg",
#       "genre_ids": [16, 18, 10752],
#       "id": 12477,
#       "original_language": "ja",
#       "original_title": "\u706b\u5782\u308b\u306e\u5893",
#       "overview": "In the final months of World War II, 14-year-old Seita and his sister Setsuko are orphaned when their mother is killed during an air raid in Kobe, Japan. After a falling out with their aunt, they move into an abandoned bomb shelter. With no surviving relatives and their emergency rations depleted, Seita and Setsuko struggle to survive.",
#       "popularity": 0.064,
#       "poster_path": "/k9tv1rXZbOhH7eiCk378x61kNQ1.jpg",
#       "release_date": "1988-04-16",
#       "title": "Grave of the Fireflies",
#       "rating": 8.456,
#       "price": 10.99,
#       "director": "Isao Takahata",
#       "main_actors": [
#         "Tsutomu Tatsumi",
#         "Ayano Shiraishi",
#         "Yoshiko Shinohara",
#         "Akemi Yamaguchi"
#       ],
#       "genres": ["Animation", "Drama", "War"],
#       "runtime": 89
#     },
#     {
#       "adult": False,
#       "backdrop_path": "/7lyq8hK0MhPHpUXdnqbFvZYSfkk.jpg",
#       "genre_ids": [18, 10749],
#       "id": 11216,
#       "original_language": "it",
#       "original_title": "Nuovo Cinema Paradiso",
#       "overview": "A filmmaker recalls his childhood, when he fell in love with the movies at his village's theater and formed a deep friendship with the theater's projectionist.",
#       "poster_path": "/gCI2AeMV4IHSewhJkzsur5MEp6R.jpg",
#       "release_date": "1988-11-17",
#       "title": "Cinema Paradiso",
      
#       "rating": 8.45,
#       "price": 8.99,
#       "director": "Giuseppe Tornatore",
#       "main_actors": [
#         "Philippe Noiret",
#         "Enzo Cannavale",
#         "Antonella Attili",
#         "Pupella Maggio",
#         "Marco Leonardi"
#       ],
#       "genres": ["Drama", "Romance"],
#       "runtime": 155
#     },
#     {
#       "adult": False,
#       "backdrop_path": "/gavyCu1UaTaTNPsVaGXT6pe5u24.jpg",
#       "genre_ids": [35, 18],
#       "id": 637,
#       "original_language": "it",
#       "original_title": "La vita \u00e8 bella",
#       "overview": "A touching story of an Italian book seller of Jewish ancestry who lives in his own little fairy tale. His creative and happy life would come to an abrupt halt when his entire family is deported to a concentration camp during World War II. While locked up he tries to convince his son that the whole thing is just a game.",
#       "poster_path": "/74hLDKjD5aGYOotO6esUVaeISa2.jpg",
#       "release_date": "1997-12-20",
#       "title": "Life Is Beautiful",
      
#       "rating": 8.448,
#       "price": 7.99,
#       "director": "Roberto Benigni",
#       "main_actors": [
#         "Roberto Benigni",
#         "Nicoletta Braschi",
#         "Giorgio Cantarini",
#         "Giustino Durano",
#         "Amerigo Fontani"
#       ],
#       "genres": ["Comedy", "Drama", "Romance"],
#       "runtime": 116
#     }
# ]


@bp.route('/')
def index():

  drama = 18 
  thriller = 53
  family = 10751

  # Query to get DVDs with a specific genre
  drama_dvd = db.session.query(DVD).join(dvd_genre_association).join(Genre).filter(Genre.id == drama).limit(3).all()
  thriller_dvd = db.session.query(DVD).join(dvd_genre_association).join(Genre).filter(Genre.id == thriller).limit(3).all()
  family_dvd = db.session.query(DVD).join(dvd_genre_association).join(Genre).filter(Genre.id == family).limit(3).all()
  
  return render_template('index.html', drama_dvd = drama_dvd, thriller_dvd=thriller_dvd, family_dvd=family_dvd)

@bp.route('/detail/<int:dvd_id>')
def detail(dvd_id):
  dvd_detail = db.session.query(DVD).filter(DVD.id == dvd_id).one()
  return render_template('detail.html', dvd = dvd_detail)

@bp.route('/movies_all')
def get_movies_all():
  dvd = DVD.query.filter(DVD.category=='movie').order_by(DVD.title).all()
  return render_template('dvd_all.html', dvd=dvd)

@bp.route('/series_all')
def get_series_all():
  dvd = DVD.query.filter(DVD.category=='series').order_by(DVD.title).all()
  return render_template('dvd_all.html', dvd=dvd)

@bp.route('/search/genres/', methods=['POST','GET'])
def get_by_genres(genre_id):
  dvd = DVD.query.filter(DVD.genres.has(id=genre_id))
  return render_template('dvd_all.html', dvd=dvd)