from flask import Blueprint, render_template
# from .models import DVD

bp = Blueprint('main', __name__)

#  MOCK_DATA
movies = [
  {
          "adult": False,
          "backdrop_path": "/kXfqcdQKsToO0OUXHcrrNCHDBzO.jpg",
          "genre_ids": [18, 80],
          "id": 278,
          "original_language": "en",
          "original_title": "The Shawshank Redemption",
          "overview": "Imprisoned in the 1940s for the double murder of his wife and her lover, upstanding banker Andy Dufresne begins a new life at the Shawshank prison, where he puts his accounting skills to work for an amoral warden. During his long stretch in prison, Dufresne comes to be admired by the other inmates -- including an older prisoner named Red -- for his integrity and unquenchable sense of hope.",
          "popularity": 166.369,
          "poster_path": "/9cqNxx0GxF0bflZmeSMuL5tnGzr.jpg",
          "release_date": "1994-09-23",
          "title": "The Shawshank Redemption",
          "director": "Frank Darabont",
          "main_actors": [
            "Tim Robbins",
            "Morgan Freeman",
            "Bob Gunton",
            "William Sadler",
            "Clancy Brown"
          ],
          "genres": ["Drama", "Crime"],
          "runtime": 142,
          "video": False,
          "vote_average": 8.707,
          "vote_count": 26926,
          "price": 9.99
        },
        {
          "adult": False,
          "backdrop_path": "/tmU7GeKVybMWFButWEGl2M4GeiP.jpg",
          "genre_ids": [18, 80],
          "id": 238,
          "original_language": "en",
          "original_title": "The Godfather",
          "overview": "Spanning the years 1945 to 1955, a chronicle of the fictional Italian-American Corleone crime family. When organized crime family patriarch, Vito Corleone barely survives an attempt on his life, his youngest son, Michael steps in to take care of the would-be killers, launching a campaign of bloody revenge.",
          "popularity": 191.591,
          "poster_path": "/3bhkrj58Vtu7enYsRolD1fZdja1.jpg",
          "release_date": "1972-03-14",
          "title": "The Godfather",
          "director": "Francis Ford Coppola",
          "main_actors": [
            "Marlon Brando",
            "Al Pacino",
            "James Caan",
            "Robert Duvall",
            "Diane Keaton"
          ],
          "genres": ["Crime", "Drama"],
          "runtime": 175,
          "video": False,
          "vote_average": 8.69,
          "vote_count": 20436,
          "price": 11.99
        },
        {
          "adult": False,
          "backdrop_path": "/kGzFbGhp99zva6oZODW5atUtnqi.jpg",
          "genre_ids": [18, 80],
          "id": 240,
          "original_language": "en",
          "original_title": "The Godfather Part II",
          "overview": "In the continuing saga of the Corleone crime family, a young Vito Corleone grows up in Sicily and in 1910s New York. In the 1950s, Michael Corleone attempts to expand the family business into Las Vegas, Hollywood and Cuba.",
          "popularity": 164.882,
          "poster_path": "/hek3koDUyRQk7FIhPXsa6mT2Zc3.jpg",
          "release_date": "1974-12-20",
          "title": "The Godfather Part II",
          "director": "Francis Ford Coppola",
          "main_actors": [
            "Al Pacino",
            "Robert De Niro",
            "Robert Duvall",
            "Diane Keaton",
            "John Cazale"
          ],
          "genres": ["Crime", "Drama"],
          "runtime": 202,
          "video": False,
          "vote_average": 8.575,
          "vote_count": 12326,
          "price": 10.99
        },
        {
          "adult": False,
          "backdrop_path": "/zb6fM1CX41D9rF9hdgclu0peUmy.jpg",
          "genre_ids": [18, 36, 10752],
          "id": 424,
          "original_language": "en",
          "original_title": "Schindler's List",
          "overview": "The true story of how businessman Oskar Schindler saved over a thousand Jewish lives from the Nazis while they worked as slaves in his factory during World War II.",
          "popularity": 78.572,
          "poster_path": "/sF1U4EUQS8YHUYjNl3pMGNIQyr0.jpg",
          "release_date": "1993-12-15",
          "title": "Schindler's List",
          "director": "Steven Spielberg",
          "main_actors": [
            "Liam Neeson",
            "Ben Kingsley",
            "Ralph Fiennes",
            "Caroline Goodall",
            "Jonathan Sagall"
          ],
          "genres": ["Biography", "Drama", "History", "War"],
          "runtime": 195,
          "video": False,
          "vote_average": 8.565,
          "vote_count": 15739,
          "price": 8.99
        },
        {
          "adult": False,
          "backdrop_path": "/qqHQsStV6exghCM7zbObuYBiYxw.jpg",
          "genre_ids": [18],
          "id": 389,
          "original_language": "en",
          "original_title": "12 Angry Men",
          "overview": "The defense and the prosecution have rested and the jury is filing into the jury room to decide if a young Spanish-American is guilty or innocent of murdering his father. What begins as an open and shut case soon becomes a mini-drama of each of the jurors' prejudices and preconceptions about the trial, the accused, and each other.",
          "popularity": 79.078,
          "poster_path": "/ow3wq89wM8qd5X7hWKxiRfsFf9C.jpg",
          "release_date": "1957-04-10",
          "title": "12 Angry Men",
          "director": "Sidney Lumet",
          "main_actors": [
            "Henry Fonda",
            "Lee J. Cobb",
            "Martin Balsam",
            "Jack Warden",
            "E.G. Marshall"
          ],
          "genres": ["Drama"],
          "runtime": 96,
          "video": False,
          "vote_average": 8.546,
          "vote_count": 8555,
          "price": 7.99
        },
        {
          "adult": False,
          "backdrop_path": "/6oaL4DP75yABrd5EbC4H2zq5ghc.jpg",
          "genre_ids": [16, 10751, 14],
          "id": 129,
          "original_language": "ja",
          "original_title": "\u5343\u3068\u5343\u5c0b\u306e\u795e\u96a0\u3057",
          "overview": "A young girl, Chihiro, becomes trapped in a strange new world of spirits. When her parents undergo a mysterious transformation, she must call upon the courage she never knew she had to free her family.",
          "popularity": 126.829,
          "poster_path": "/39wmItIWsg5sZMyRUHLkWBcuVCM.jpg",
          "release_date": "2001-07-20",
          "title": "Spirited Away",
          "director": "Hayao Miyazaki",
          "main_actors": [
            "Rumi Hiiragi",
            "Miyu Irino",
            "Mari Natsuki",
            "Takeshi Naito",
            "Yasuko Sawaguchi"
          ],
          "genres": ["Animation", "Family", "Fantasy"],
          "runtime": 125,
          "video": False,
          "vote_average": 8.537,
          "vote_count": 16382,
          "price": 9.99
        },
        {
          "adult": False,
          "backdrop_path": "/90ez6ArvpO8bvpyIngBuwXOqJm5.jpg",
          "genre_ids": [35, 18, 10749],
          "id": 19404,
          "original_language": "hi",
          "original_title": "\u0926\u093f\u0932\u0935\u093e\u0932\u0947 \u0926\u0941\u0932\u094d\u0939\u0928\u093f\u092f\u093e \u0932\u0947 \u091c\u093e\u092f\u0947\u0902\u0917\u0947",
          "overview": "Raj is a rich, carefree, happy-go-lucky second generation NRI. Simran is the daughter of Chaudhary Baldev Singh, who in spite of being an NRI is very strict about adherence to Indian values. Simran has left for India to be married to her childhood fianc\u00e9. Raj leaves for India with a mission at his hands, to claim his lady love under the noses of her whole family. Thus begins a saga.",
          "popularity": 37.563,
          "poster_path": "/lfRkUr7DYdHldAqi3PwdQGBRBPM.jpg",
          "release_date": "1995-10-20",
          "title": "Dilwale Dulhania Le Jayenge",
          "director": "Aditya Chopra",
          "main_actors": [
            "Shah Rukh Khan",
            "Kajol",
            "Amrish Puri",
            "Farida Jalal",
            "Anupam Kher"
          ],
          "genres": ["Comedy", "Drama", "Romance"],
          "runtime": 190,
          "video": False,
          "vote_average": 8.529,
          "vote_count": 4429,
          "price": 11.99
        },
        {
          "adult": False,
          "backdrop_path": "/nMKdUUepR0i5zn0y1T4CsSB5chy.jpg",
          "genre_ids": [18, 28, 80, 53],
          "id": 155,
          "original_language": "en",
          "original_title": "The Dark Knight",
          "overview": "Batman raises the stakes in his war on crime. With the help of Lt. Jim Gordon and District Attorney Harvey Dent, Batman sets out to dismantle the remaining criminal organizations that plague the streets. The partnership proves to be effective, but they soon find themselves prey to a reign of chaos unleashed by a rising criminal mastermind known to the terrified citizens of Gotham as the Joker.",
          "popularity": 181.169,
          "poster_path": "/qJ2tW6WMUDux911r6m7haRef0WH.jpg",
          "release_date": "2008-07-16",
          "title": "The Dark Knight",
          "director": "Christopher Nolan",
          "main_actors": [
            "Christian Bale",
            "Heath Ledger",
            "Aaron Eckhart",
            "Michael Caine",
            "Maggie Gyllenhaal"
          ],
          "genres": ["Action", "Crime", "Drama", "Thriller"],
          "runtime": 152,
          "video": False,
          "vote_average": 8.515,
          "vote_count": 32672,
          "price": 10.99
        },
        {
          "adult": False,
          "backdrop_path": "/8eihUxjQsJ7WvGySkVMC0EwbPAD.jpg",
          "genre_ids": [35, 53, 18],
          "id": 496243,
          "original_language": "ko",
          "original_title": "\uae30\uc0dd\ucda9",
          "overview": "All unemployed, Ki-taek's family takes peculiar interest in the wealthy and glamorous Parks for their livelihood until they get entangled in an unexpected incident.",
          "popularity": 73.293,
          "poster_path": "/7IiTTgloJzvGI1TAYymCfbfl3vT.jpg",
          "release_date": "2019-05-30",
          "title": "Parasite",
          "director": "Bong Joon-ho",
          "main_actors": [
            "Song Kang-ho",
            "Lee Sun-kyun",
            "Cho Yeo-jeong",
            "Choi Woo-shik",
            "Park So-dam"
          ],
          "genres": ["Comedy", "Drama", "Thriller"],
          "runtime": 132,
          "video": False,
          "vote_average": 8.506,
          "vote_count": 18091,
          "price": 8.99
        },
        {
          "adult": False,
          "backdrop_path": "/vxJ08SvwomfKbpboCWynC3uqUg4.jpg",
          "genre_ids": [14, 18, 80],
          "id": 497,
          "original_language": "en",
          "original_title": "The Green Mile",
          "overview": "A supernatural tale set on death row in a Southern prison, where gentle giant John Coffey possesses the mysterious power to heal people's ailments. When the cell block's head guard, Paul Edgecomb, recognizes Coffey's miraculous gift, he tries desperately to help stave off the condemned man's execution.",
          "popularity": 66.337,
          "poster_path": "/8VG8fDNiy50H4FedGwdSVUPoaJe.jpg",
          "release_date": "1999-12-10",
          "title": "The Green Mile",
          "director": "Frank Darabont",
          "main_actors": [
            "Tom Hanks",
            "Michael Clarke Duncan",
            "David Morse",
            "Bonnie Hunt",
            "James Cromwell"
          ],
          "genres": ["Crime", "Drama", "Fantasy"],
          "runtime": 189,
          "video": False,
          "vote_average": 8.5,
          "vote_count": 17281,
          "price": 7.99
        },
        {
            "adult": False,
            "backdrop_path": "/suaEOtk1N1sgg2MTM7oZd2cfVp3.jpg",
            "genre_ids": [
                53,
                80
            ],
            "id": 680,
            "original_language": "en",
            "original_title": "Pulp Fiction",
            "overview": "A burger-loving hit man, his philosophical partner, a drug-addled gangster's moll and a washed-up boxer converge in this sprawling, comedic crime caper. Their adventures unfurl in three stories that ingeniously trip back and forth in time.",
            "popularity": 91.822,
            "poster_path": "/d5iIlFn5s0ImszYzBPb8JPIfbXD.jpg",
            "release_date": "1994-09-10",
            "title": "Pulp Fiction",
            "video": False,
            "vote_average": 8.5,
            "vote_count": 27719,
            "price": 9.99
        },
        {
            "adult": False,
            "backdrop_path": "/dIWwZW7dJJtqC6CgWzYkNVKIUm8.jpg",
            "genre_ids": [
                16,
                10749,
                18
            ],
            "id": 372058,
            "original_language": "ja",
            "original_title": "\u541b\u306e\u540d\u306f\u3002",
            "overview": "High schoolers Mitsuha and Taki are complete strangers living separate lives. But one night, they suddenly switch places. Mitsuha wakes up in Taki\u2019s body, and he in hers. This bizarre occurrence continues to happen randomly, and the two must adjust their lives around each other.",
            "popularity": 75.563,
            "poster_path": "/vfJFJPepRKapMd5G2ro7klIRysq.jpg",
            "release_date": "2016-08-26",
            "title": "Your Name.",
            "video": False,
            "vote_average": 8.486,
            "vote_count": 11282,
            "price": 11.99
        },
        {
            "adult": False,
            "backdrop_path": "/2u7zbn8EudG6kLlBzUYqP8RyFU4.jpg",
            "genre_ids": [
                12,
                14,
                28
            ],
            "id": 122,
            "original_language": "en",
            "original_title": "The Lord of the Rings: The Return of the King",
            "overview": "As armies mass for a final battle that will decide the fate of the world--and powerful, ancient forces of Light and Dark compete to determine the outcome--one member of the Fellowship of the Ring is revealed as the noble heir to the throne of the Kings of Men. Yet, the sole hope for triumph over evil lies with a brave hobbit, Frodo, who, accompanied by his loyal friend Sam and the hideous, wretched Gollum, ventures deep into the very dark heart of Mordor on his seemingly impossible quest to destroy the Ring of Power.\u200b",
            "popularity": 205.431,
            "poster_path": "/rCzpDGLbOoPwLjy3OAm5NUPOTrC.jpg",
            "release_date": "2003-12-17",
            "title": "The Lord of the Rings: The Return of the King",
            "video": False,
            "vote_average": 8.482,
            "vote_count": 24016,
            "price": 10.99
        },
        {
            "adult": False,
            "backdrop_path": "/ghgfzbEV7kbpbi1O8eIILKVXEA8.jpg",
            "genre_ids": [
                35,
                18,
                10749
            ],
            "id": 13,
            "original_language": "en",
            "original_title": "Forrest Gump",
            "overview": "A man with a low IQ has accomplished great things in his life and been present during significant historic events\u2014in each case, far exceeding what anyone imagined he could do. But despite all he has achieved, his one true love eludes him.",
            "popularity": 106.538,
            "poster_path": "/arw2vcBveWOVZr6pxd9XTd1TdQa.jpg",
            "release_date": "1994-06-23",
            "title": "Forrest Gump",
            "video": False,
            "vote_average": 8.472,
            "vote_count": 27249,
            "price": 8.99
        },
        {
            "adult": False,
            "backdrop_path": "/7TF4p86ZafnxFuNqWdhpHXFO244.jpg",
            "genre_ids": [
                18,
                80
            ],
            "id": 769,
            "original_language": "en",
            "original_title": "GoodFellas",
            "overview": "The true story of Henry Hill, a half-Irish, half-Sicilian Brooklyn kid who is adopted by neighbourhood gangsters at an early age and climbs the ranks of a Mafia family under the guidance of Jimmy Conway.",
            "popularity": 96.484,
            "poster_path": "/aKuFiU82s5ISJpGZp7YkIr3kCUd.jpg",
            "release_date": "1990-09-12",
            "title": "GoodFellas",
            "video": False,
            "vote_average": 8.5,
            "vote_count": 12764,
            "price": 7.99
        },
        {
            "adult": False,
            "backdrop_path": "/Adrip2Jqzw56KeuV2nAxucKMNXA.jpg",
            "genre_ids": [
                37
            ],
            "id": 429,
            "original_language": "it",
            "original_title": "Il buono, il brutto, il cattivo",
            "overview": "While the Civil War rages on between the Union and the Confederacy, three men \u2013 a quiet loner, a ruthless hitman, and a Mexican bandit \u2013 comb the American Southwest in search of a strongbox containing $200,000 in stolen gold.",
            "popularity": 70.751,
            "poster_path": "/bX2xnavhMYjWDoZp1VM6VnU1xwe.jpg",
            "release_date": "1966-12-22",
            "title": "The Good, the Bad and the Ugly",
            "video": False,
            "vote_average": 8.462,
            "vote_count": 8533,
            "price": 9.99
        },
        {
            "adult": False,
            "backdrop_path": "/sJNNMCc6B7KZIY3LH3JMYJJNH5j.jpg",
            "genre_ids": [
                28,
                18
            ],
            "id": 346,
            "original_language": "ja",
            "original_title": "\u4e03\u4eba\u306e\u4f8d",
            "overview": "A samurai answers a village's request for protection after he falls on hard times. The town needs protection from bandits, so the samurai gathers six others to help him teach the people how to defend themselves, and the villagers provide the soldiers with food.",
            "popularity": 39.49,
            "poster_path": "/8OKmBV5BUFzmozIC3pPWKHy17kx.jpg",
            "release_date": "1954-04-26",
            "title": "Seven Samurai",
            "video": False,
            "vote_average": 8.5,
            "vote_count": 3632,
            "price": 11.99
        },
        {
            "adult": False,
            "backdrop_path": "/gwj4R8Uy1GwejKqfofREKI9Jh7L.jpg",
            "genre_ids": [
                16,
                18,
                10752
            ],
            "id": 12477,
            "original_language": "ja",
            "original_title": "\u706b\u5782\u308b\u306e\u5893",
            "overview": "In the final months of World War II, 14-year-old Seita and his sister Setsuko are orphaned when their mother is killed during an air raid in Kobe, Japan. After a falling out with their aunt, they move into an abandoned bomb shelter. With no surviving relatives and their emergency rations depleted, Seita and Setsuko struggle to survive.",
            "popularity": 0.064,
            "poster_path": "/k9tv1rXZbOhH7eiCk378x61kNQ1.jpg",
            "release_date": "1988-04-16",
            "title": "Grave of the Fireflies",
            "video": False,
            "vote_average": 8.456,
            "vote_count": 5470,
            "price": 10.99
        },
        {
            "adult": False,
            "backdrop_path": "/7lyq8hK0MhPHpUXdnqbFvZYSfkk.jpg",
            "genre_ids": [
                18,
                10749
            ],
            "id": 11216,
            "original_language": "it",
            "original_title": "Nuovo Cinema Paradiso",
            "overview": "A filmmaker recalls his childhood, when he fell in love with the movies at his village's theater and formed a deep friendship with the theater's projectionist.",
            "popularity": 44.111,
            "poster_path": "/gCI2AeMV4IHSewhJkzsur5MEp6R.jpg",
            "release_date": "1988-11-17",
            "title": "Cinema Paradiso",
            "video": False,
            "vote_average": 8.45,
            "vote_count": 4325,
            "price": 8.99
        },
        {
            "adult": False,
            "backdrop_path": "/gavyCu1UaTaTNPsVaGXT6pe5u24.jpg",
            "genre_ids": [
                35,
                18
            ],
            "id": 637,
            "original_language": "it",
            "original_title": "La vita \u00e8 bella",
            "overview": "A touching story of an Italian book seller of Jewish ancestry who lives in his own little fairy tale. His creative and happy life would come to an abrupt halt when his entire family is deported to a concentration camp during World War II. While locked up he tries to convince his son that the whole thing is just a game.",
            "popularity": 61.57,
            "poster_path": "/74hLDKjD5aGYOotO6esUVaeISa2.jpg",
            "release_date": "1997-12-20",
            "title": "Life Is Beautiful",
            "video": False,
            "vote_average": 8.448,
            "vote_count": 12945,
            "price": 7.99
        }
]
tv_series = [
  {
            "adult": False,
            "backdrop_path": "/9faGSFi5jam6pDWGNd0p8JcJgXQ.jpg",
            "genre_ids": [
                18,
                80
            ],
            "id": 1396,
            "origin_country": [
                "US"
            ],
            "original_language": "en",
            "original_name": "Breaking Bad",
            "overview": "Walter White, a New Mexico chemistry teacher, is diagnosed with Stage III cancer and given a prognosis of only two years left to live. He becomes filled with a sense of fearlessness and an unrelenting desire to secure his family's financial future at any cost as he enters the dangerous world of drugs and crime.",
            "popularity": 478.531,
            "poster_path": "/ztkUQFLlC19CCMYHW9o1zWhJRNq.jpg",
            "first_air_date": "2008-01-20",
            "name": "Breaking Bad",
            "vote_average": 8.915,
            "vote_count": 14282
        },
        {
            "adult": False,
            "backdrop_path": "/tuCU2yVRM2iZxFkpqlPUyvd6tSu.jpg",
            "genre_ids": [
                16,
                35,
                10765
            ],
            "id": 94954,
            "origin_country": [
                "US"
            ],
            "original_language": "en",
            "original_name": "Hazbin Hotel",
            "overview": "In attempt to find a non-violent alternative for reducing Hell's overpopulation, the daughter of Lucifer opens a rehabilitation hotel that offers a group of misfit demons a chance at redemption.",
            "popularity": 100.352,
            "poster_path": "/rXojaQcxVUubPLSrFV8PD4xdjrs.jpg",
            "first_air_date": "2024-01-18",
            "name": "Hazbin Hotel",
            "vote_average": 8.851,
            "vote_count": 1101
        },
        {
            "adult": False,
            "backdrop_path": "/96RT2A47UdzWlUfvIERFyBsLhL2.jpg",
            "genre_ids": [
                16,
                10759,
                10765
            ],
            "id": 209867,
            "origin_country": [
                "JP"
            ],
            "original_language": "ja",
            "original_name": "\u846c\u9001\u306e\u30d5\u30ea\u30fc\u30ec\u30f3",
            "overview": "After the party of heroes defeated the Demon King, they restored peace to the land and returned to lives of solitude. Generations pass, and the elven mage Frieren comes face to face with humanity\u2019s mortality. She takes on a new apprentice and promises to fulfill old friends\u2019 dying wishes. Can an elven mind make peace with the nature of life and death? Frieren embarks on her quest to find out.",
            "popularity": 141.388,
            "poster_path": "/dqZENchTd7lp5zht7BdlqM7RBhD.jpg",
            "first_air_date": "2023-09-29",
            "name": "Frieren: Beyond Journey's End",
            "vote_average": 8.834,
            "vote_count": 290
        },
        {
            "adult": False,
            "backdrop_path": "/wQEW3xLrQAThu1GvqpsKQyejrYS.jpg",
            "genre_ids": [
                16,
                10765,
                10759,
                9648
            ],
            "id": 94605,
            "origin_country": [
                "US"
            ],
            "original_language": "en",
            "original_name": "Arcane",
            "overview": "Amid the stark discord of twin cities Piltover and Zaun, two sisters fight on rival sides of a war between magic technologies and clashing convictions.",
            "popularity": 107.318,
            "poster_path": "/fqldf2t8ztc9aiwn3k6mlX3tvRT.jpg",
            "first_air_date": "2021-11-06",
            "name": "Arcane",
            "vote_average": 8.749,
            "vote_count": 4005
        },
        {
            "adult": False,
            "backdrop_path": "/kU98MbVVgi72wzceyrEbClZmMFe.jpg",
            "genre_ids": [
                16,
                10759,
                10765
            ],
            "id": 246,
            "origin_country": [
                "US"
            ],
            "original_language": "en",
            "original_name": "Avatar: The Last Airbender",
            "overview": "In a war-torn world of elemental magic, a young boy reawakens to undertake a dangerous mystic quest to fulfill his destiny as the Avatar, and bring peace to the world.",
            "popularity": 102.632,
            "poster_path": "/9jUuxbMSp3cwC2DDrSAs2F43Ric.jpg",
            "first_air_date": "2005-02-21",
            "name": "Avatar: The Last Airbender",
            "vote_average": 8.7,
            "vote_count": 4087
        },
        {
            "adult": False,
            "backdrop_path": "/a6ptrTUH1c5OdWanjyYtAkOuYD0.jpg",
            "genre_ids": [
                10759,
                35,
                16
            ],
            "id": 37854,
            "origin_country": [
                "JP"
            ],
            "original_language": "ja",
            "original_name": "\u30ef\u30f3\u30d4\u30fc\u30b9",
            "overview": "Years ago, the fearsome Pirate King, Gol D. Roger was executed leaving a huge pile of treasure and the famous \"One Piece\" behind. Whoever claims the \"One Piece\" will be named the new King of the Pirates.\n\nMonkey D. Luffy, a boy who consumed a \"Devil Fruit,\" decides to follow in the footsteps of his idol, the pirate Shanks, and find the One Piece. It helps, of course, that his body has the properties of rubber and that he's surrounded by a bevy of skilled fighters and thieves to help him along the way.\n\nLuffy will do anything to get the One Piece and become King of the Pirates!",
            "popularity": 133.568,
            "poster_path": "/cMD9Ygz11zjJzAovURpO75Qg7rT.jpg",
            "first_air_date": "1999-10-20",
            "name": "One Piece",
            "vote_average": 8.7,
            "vote_count": 4641
        },
        {
            "adult": False,
            "backdrop_path": "/rBF8wVQN8hTWHspVZBlI3h7HZJ.jpg",
            "genre_ids": [
                16,
                35,
                10765,
                10759
            ],
            "id": 60625,
            "origin_country": [
                "US"
            ],
            "original_language": "en",
            "original_name": "Rick and Morty",
            "overview": "Rick is a mentally-unbalanced but scientifically gifted old man who has recently reconnected with his family. He spends most of his time involving his young grandson Morty in dangerous, outlandish adventures throughout space and alternate universes. Compounded with Morty's already unstable family life, these events cause Morty much distress at home and school.",
            "popularity": 385.418,
            "poster_path": "/gdIrmf2DdY5mgN6ycVP0XlzKzbE.jpg",
            "first_air_date": "2013-12-02",
            "name": "Rick and Morty",
            "vote_average": 8.697,
            "vote_count": 9704
        },
        {
            "adult": False,
            "backdrop_path": "/A6tMQAo6t6eRFCPhsrShmxZLqFB.jpg",
            "genre_ids": [
                10759,
                16,
                10765,
                35
            ],
            "id": 31911,
            "origin_country": [
                "JP"
            ],
            "original_language": "ja",
            "original_name": "\u92fc\u306e\u932c\u91d1\u8853\u5e2b FULLMETAL ALCHEMIST",
            "overview": "Disregard for alchemy\u2019s laws ripped half of Edward Elric\u2019s limbs from his body and left his brother Alphonse\u2019s soul clinging to a suit of armor. To restore what was lost, the brothers seek the Philosopher\u2019s Stone. Enemies and allies \u2013 the corrupt military, the Homunculi, and foreign alchemists \u2013 will alter the Elric brothers course, but their purpose will remain unchanged and their bond unbreakable.",
            "popularity": 166.821,
            "poster_path": "/8H4ej2NpujYVBPsW2smmzC8d2xU.jpg",
            "first_air_date": "2009-04-05",
            "name": "Fullmetal Alchemist: Brotherhood",
            "vote_average": 8.7,
            "vote_count": 2032
        },
        {
            "adult": False,
            "backdrop_path": "/hPea3Qy5Gd6z4kJLUruBbwAH8Rm.jpg",
            "genre_ids": [
                80,
                18
            ],
            "id": 60059,
            "origin_country": [
                "US"
            ],
            "original_language": "en",
            "original_name": "Better Call Saul",
            "overview": "Six years before Saul Goodman meets Walter White. We meet him when the man who will become Saul Goodman is known as Jimmy McGill, a small-time lawyer searching for his destiny, and, more immediately, hustling to make ends meet. Working alongside, and, often, against Jimmy, is \u201cfixer\u201d Mike Ehrmantraut. The series tracks Jimmy\u2019s transformation into Saul Goodman, the man who puts \u201ccriminal\u201d in \u201ccriminal lawyer\".",
            "popularity": 250.579,
            "poster_path": "/fC2HDm5t0kHl7mTm7jxMR31b7by.jpg",
            "first_air_date": "2015-02-08",
            "name": "Better Call Saul",
            "vote_average": 8.688,
            "vote_count": 5169
        },
        {
            "adult": False,
            "backdrop_path": "/900tHlUYUkp7Ol04XFSoAaEIXcT.jpg",
            "genre_ids": [
                18
            ],
            "id": 87108,
            "origin_country": [
                "US"
            ],
            "original_language": "en",
            "original_name": "Chernobyl",
            "overview": "The true story of one of the worst man-made catastrophes in history: the catastrophic nuclear accident at Chernobyl. A tale of the brave men and women who sacrificed to save Europe from unimaginable disaster.",
            "popularity": 86.683,
            "poster_path": "/hlLXt2tOPT6RRnjiUmoxyG1LTFi.jpg",
            "first_air_date": "2019-05-06",
            "name": "Chernobyl",
            "vote_average": 8.7,
            "vote_count": 6255
        },
        {
            "adult": False,
            "backdrop_path": "/70YdbMELM4b8x8VXjlubymb2bQ0.jpg",
            "genre_ids": [
                18,
                10751
            ],
            "id": 70785,
            "origin_country": [
                "CA"
            ],
            "original_language": "en",
            "original_name": "Anne with an E",
            "overview": "A coming-of-age story about an outsider who, against all odds and numerous challenges, fights for love and acceptance and for her place in the world. The series centers on a young orphaned girl in the late 1890\u2019s, who, after an abusive childhood spent in orphanages and the homes of strangers, is mistakenly sent to live with an elderly woman and her aging brother. Over time, 13-year-old Anne will transform their lives and eventually the small town in which they live with her unique spirit, fierce intellect and brilliant imagination.",
            "popularity": 99.966,
            "poster_path": "/6P6tXhjT5tK3qOXzxF9OMLlG7iz.jpg",
            "first_air_date": "2017-03-19",
            "name": "Anne with an E",
            "vote_average": 8.7,
            "vote_count": 4630
        },
        {
            "adult": False,
            "backdrop_path": "/cHyY5z4txdVyGtYMvBJhCqCcJso.jpg",
            "genre_ids": [
                16,
                10765,
                18,
                10759,
                35,
                10762
            ],
            "id": 92685,
            "origin_country": [
                "US"
            ],
            "original_language": "en",
            "original_name": "The Owl House",
            "overview": "An animated fantasy-comedy series that follows Luz, a self-assured teenage girl who accidentally stumbles upon a portal to a magical world where she befriends a rebellious witch, Eda, and an adorably tiny warrior, King. Despite not having magical abilities, Luz pursues her dream of becoming a witch by serving as Eda's apprentice at the Owl House and ultimately finds a new family in an unlikely setting.",
            "popularity": 108.445,
            "poster_path": "/zhdy3PcNVE15wj1wrxn45ARZBnx.jpg",
            "first_air_date": "2020-01-10",
            "name": "The Owl House",
            "vote_average": 8.665,
            "vote_count": 1578
        },
        {
            "adult": False,
            "backdrop_path": "/xdTwlG8MYAOkFuAGUqt8LgmgTNZ.jpg",
            "genre_ids": [
                16,
                35,
                10765
            ],
            "id": 62741,
            "origin_country": [
                "JP"
            ],
            "original_language": "ja",
            "original_name": "\u795e\u69d8\u306f\u3058\u3081\u307e\u3057\u305f",
            "overview": "Nanami was just a normal high school girl down on her luck until a stranger\u2019s lips marked her as the new Land God and turned her world upside down. Now, she\u2019s figuring out the duties of a deity with the help of Tomoe, a reformed fox demon who reluctantly becomes her familiar in a contract sealed with a kiss. The new responsibilities\u2014and boys\u2014are a lot to handle, like the crow demon masquerading as a gorgeous pop idol and the adorable snake spirit who\u2019s chosen the newly minted god to be his bride. As the headstrong Tomoe tries to whip her into shape, Nanami finds that love just might have cute, pointed fox ears. With romance in the air, will the human deity be able to prove herself worthy of her new title?",
            "popularity": 60.764,
            "poster_path": "/5E7GL8KxpFemEFl3Lv8Fu4RuSwa.jpg",
            "first_air_date": "2012-10-02",
            "name": "Kamisama Kiss",
            "vote_average": 8.7,
            "vote_count": 885
        },
        {
            "adult": False,
            "backdrop_path": "/3GQKYh6Trm8pxd2AypovoYQf4Ay.jpg",
            "genre_ids": [
                16,
                10759,
                10765
            ],
            "id": 85937,
            "origin_country": [
                "JP"
            ],
            "original_language": "ja",
            "original_name": "\u9b3c\u6ec5\u306e\u5203",
            "overview": "It is the Taisho Period in Japan. Tanjiro, a kindhearted boy who sells charcoal for a living, finds his family slaughtered by a demon. To make matters worse, his younger sister Nezuko, the sole survivor, has been transformed into a demon herself. Though devastated by this grim reality, Tanjiro resolves to become a \u201cdemon slayer\u201d so that he can turn his sister back into a human, and kill the demon that massacred his family.",
            "popularity": 98.148,
            "poster_path": "/xUfRZu2mi8jH6SzQEJGP6tjBuYj.jpg",
            "first_air_date": "2019-04-06",
            "name": "Demon Slayer: Kimetsu no Yaiba",
            "vote_average": 8.658,
            "vote_count": 6409
        },
        {
            "adult": False,
            "backdrop_path": "/rqbCbjB19amtOtFQbb3K2lgm2zv.jpg",
            "genre_ids": [
                16,
                10765,
                10759
            ],
            "id": 1429,
            "origin_country": [
                "JP"
            ],
            "original_language": "ja",
            "original_name": "\u9032\u6483\u306e\u5de8\u4eba",
            "overview": "Many years ago, the last remnants of humanity were forced to retreat behind the towering walls of a fortified city to escape the massive, man-eating Titans that roamed the land outside their fortress. Only the heroic members of the Scouting Legion dared to stray beyond the safety of the walls \u2013 but even those brave warriors seldom returned alive. Those within the city clung to the illusion of a peaceful existence until the day that dream was shattered, and their slim chance at survival was reduced to one horrifying choice: kill \u2013 or be devoured!",
            "popularity": 127.928,
            "poster_path": "/hTP1DtLGFamjfu8WqjnuQdP1n4i.jpg",
            "first_air_date": "2013-04-07",
            "name": "Attack on Titan",
            "vote_average": 8.7,
            "vote_count": 6346
        },
        {
            "adult": False,
            "backdrop_path": "/2w8FaLwwJTWr6ExUMeVgT2Th5YT.jpg",
            "genre_ids": [
                16,
                35,
                18,
                10759
            ],
            "id": 42705,
            "origin_country": [
                "JP"
            ],
            "original_language": "ja",
            "original_name": "\u306f\u3058\u3081\u306e\u4e00\u6b69",
            "overview": "Makunouchi Ippo is an ordinary high school student in Japan. Since he spends most of his time away from school helping his mother run the family business, he doesn't get to enjoy his younger years like most teenagers. Always a target for bullying at school (the family fishing business grants him a distinct odor), Ippo's life is one of hardship. One of these after-school bullying sessions turns Ippo's life around for the better, as he is saved by a boxer named Takamura. He decides to follow in Takamura's footsteps and train to become a boxer, giving his life direction and purpose. Ippo's path to perfecting his pugilistic prowess is just beginning...",
            "popularity": 200.373,
            "poster_path": "/qC4taY6yB9BWJ8IxcbnXR8yUS4o.jpg",
            "first_air_date": "2000-10-03",
            "name": "Fighting Spirit",
            "vote_average": 8.654,
            "vote_count": 1044
        },
        {
            "adult": False,
            "backdrop_path": "/3MC8VIxq8u1vKOKTfz6FtrFXuMZ.jpg",
            "genre_ids": [
                10765,
                18,
                10759,
                9648
            ],
            "id": 135157,
            "origin_country": [
                "KR"
            ],
            "original_language": "ko",
            "original_name": "\ud658\ud63c",
            "overview": "A powerful sorceress in a blind woman's body encounters a man from a prestigious family, who wants her help to change his destiny.",
            "popularity": 131.772,
            "poster_path": "/q2IiPRSXPOZ6qVRj36WRAYEQyHs.jpg",
            "first_air_date": "2022-06-18",
            "name": "Alchemy of Souls",
            "vote_average": 8.65,
            "vote_count": 579
        },
        {
            "adult": False,
            "backdrop_path": "/7BoRhg8zXP0ca9Zql4p8llCFR2P.jpg",
            "genre_ids": [
                18,
                10765,
                35
            ],
            "id": 221851,
            "origin_country": [
                "KR"
            ],
            "original_language": "ko",
            "original_name": "\ub0b4 \ub0a8\ud3b8\uacfc \uacb0\ud63c\ud574\uc918",
            "overview": "Kang Ji-won, a terminally ill cancer patient, is killed by her husband and best friend after she witnesses them having an affair. She wakes up 10 years before the incident and decides to seek revenge with the help of Yu Ji-hyuk, a director at the company where she works. Now, she must reclaim her fate and eliminate the trash from her life.",
            "popularity": 102.858,
            "poster_path": "/y2hvE76S6Me0uhYEQ1P8lGf7Wm0.jpg",
            "first_air_date": "2024-01-01",
            "name": "Marry My Husband",
            "vote_average": 8.648,
            "vote_count": 423
        },
        {
            "adult": False,
            "backdrop_path": "/j0viazcPT7Te2XC7iomH9lBtiVG.jpg",
            "genre_ids": [
                35,
                18
            ],
            "id": 68349,
            "origin_country": [
                "KR"
            ],
            "original_language": "ko",
            "original_name": "\uc5ed\ub3c4\uc694\uc815 \uae40\ubcf5\uc8fc",
            "overview": "A competitive swimmer crosses paths with his childhood friend, a rising weight lifting star, and realizes that she has a secret crush on his cousin.",
            "popularity": 53.907,
            "poster_path": "/kyZKEtDNBS5S3ZobqJssdhUYUfv.jpg",
            "first_air_date": "2016-11-16",
            "name": "Weightlifting Fairy Kim Bok-joo",
            "vote_average": 8.6,
            "vote_count": 804
        },
        {
            "adult": False,
            "backdrop_path": "/dfmPbyeZZSz3bekeESvMJaH91gS.jpg",
            "genre_ids": [
                16,
                10765,
                10759,
                18
            ],
            "id": 95557,
            "origin_country": [
                "US"
            ],
            "original_language": "en",
            "original_name": "INVINCIBLE",
            "overview": "Mark Grayson is a normal teenager except for the fact that his father is the most powerful superhero on the planet. Shortly after his seventeenth birthday, Mark begins to develop powers of his own and enters into his father\u2019s tutelage.",
            "popularity": 100.123,
            "poster_path": "/dMOpdkrDC5dQxqNydgKxXjBKyAc.jpg",
            "first_air_date": "2021-03-25",
            "name": "INVINCIBLE",
            "vote_average": 8.6,
            "vote_count": 4424
        }
]
dvd = [
  {
    "adult": False,
    "backdrop_path": "/kXfqcdQKsToO0OUXHcrrNCHDBzO.jpg",
    "genre_ids": [18, 80],
    "id": 278,
    "original_language": "en",
    "original_title": "The Shawshank Redemption",
    "overview": "Imprisoned in the 1940s for the double murder of his wife and her lover, upstanding banker Andy Dufresne begins a new life at the Shawshank prison, where he puts his accounting skills to work for an amoral warden. During his long stretch in prison, Dufresne comes to be admired by the other inmates -- including an older prisoner named Red -- for his integrity and unquenchable sense of hope.",
    "popularity": 166.369,
    "poster_path": "/9cqNxx0GxF0bflZmeSMuL5tnGzr.jpg",
    "release_date": "1994-09-23",
    "title": "The Shawshank Redemption",
    "director": "Frank Darabont",
    "main_actors": [
      "Tim Robbins",
      "Morgan Freeman",
      "Bob Gunton",
      "William Sadler",
      "Clancy Brown"
    ],
    "genres": ["Drama", "Crime"],
    "runtime": 142,
    "video": False,
    "vote_average": 8.707,
    "vote_count": 26926,
    "price": 9.99
  },
  {
    "adult": False,
    "backdrop_path": "/tmU7GeKVybMWFButWEGl2M4GeiP.jpg",
    "genre_ids": [18, 80],
    "id": 238,
    "original_language": "en",
    "original_title": "The Godfather",
    "overview": "Spanning the years 1945 to 1955, a chronicle of the fictional Italian-American Corleone crime family. When organized crime family patriarch, Vito Corleone barely survives an attempt on his life, his youngest son, Michael steps in to take care of the would-be killers, launching a campaign of bloody revenge.",
    "popularity": 191.591,
    "poster_path": "/3bhkrj58Vtu7enYsRolD1fZdja1.jpg",
    "release_date": "1972-03-14",
    "title": "The Godfather",
    "director": "Francis Ford Coppola",
    "main_actors": [
      "Marlon Brando",
      "Al Pacino",
      "James Caan",
      "Robert Duvall",
      "Diane Keaton"
    ],
    "genres": ["Crime", "Drama"],
    "runtime": 175,
    "video": False,
    "vote_average": 8.69,
    "vote_count": 20436,
    "price": 11.99
  },
  {
    "adult": False,
    "backdrop_path": "/kGzFbGhp99zva6oZODW5atUtnqi.jpg",
    "genre_ids": [18, 80],
    "id": 240,
    "original_language": "en",
    "original_title": "The Godfather Part II",
    "overview": "In the continuing saga of the Corleone crime family, a young Vito Corleone grows up in Sicily and in 1910s New York. In the 1950s, Michael Corleone attempts to expand the family business into Las Vegas, Hollywood and Cuba.",
    "popularity": 164.882,
    "poster_path": "/hek3koDUyRQk7FIhPXsa6mT2Zc3.jpg",
    "release_date": "1974-12-20",
    "title": "The Godfather Part II",
    "director": "Francis Ford Coppola",
    "main_actors": [
      "Al Pacino",
      "Robert De Niro",
      "Robert Duvall",
      "Diane Keaton",
      "John Cazale"
    ],
    "genres": ["Crime", "Drama"],
    "runtime": 202,
    "video": False,
    "vote_average": 8.575,
    "vote_count": 12326,
    "price": 10.99
  },
  {
    "adult": False,
    "backdrop_path": "/zb6fM1CX41D9rF9hdgclu0peUmy.jpg",
    "genre_ids": [18, 36, 10752],
    "id": 424,
    "original_language": "en",
    "original_title": "Schindler's List",
    "overview": "The true story of how businessman Oskar Schindler saved over a thousand Jewish lives from the Nazis while they worked as slaves in his factory during World War II.",
    "popularity": 78.572,
    "poster_path": "/sF1U4EUQS8YHUYjNl3pMGNIQyr0.jpg",
    "release_date": "1993-12-15",
    "title": "Schindler's List",
    "director": "Steven Spielberg",
    "main_actors": [
      "Liam Neeson",
      "Ben Kingsley",
      "Ralph Fiennes",
      "Caroline Goodall",
      "Jonathan Sagall"
    ],
    "genres": ["Biography", "Drama", "History", "War"],
    "runtime": 195,
    "video": False,
    "vote_average": 8.565,
    "vote_count": 15739,
    "price": 8.99
  },
  {
    "adult": False,
    "backdrop_path": "/qqHQsStV6exghCM7zbObuYBiYxw.jpg",
    "genre_ids": [18],
    "id": 389,
    "original_language": "en",
    "original_title": "12 Angry Men",
    "overview": "The defense and the prosecution have rested and the jury is filing into the jury room to decide if a young Spanish-American is guilty or innocent of murdering his father. What begins as an open and shut case soon becomes a mini-drama of each of the jurors' prejudices and preconceptions about the trial, the accused, and each other.",
    "popularity": 79.078,
    "poster_path": "/ow3wq89wM8qd5X7hWKxiRfsFf9C.jpg",
    "release_date": "1957-04-10",
    "title": "12 Angry Men",
    "director": "Sidney Lumet",
    "main_actors": [
      "Henry Fonda",
      "Lee J. Cobb",
      "Martin Balsam",
      "Jack Warden",
      "E.G. Marshall"
    ],
    "genres": ["Drama"],
    "runtime": 96,
    "video": False,
    "vote_average": 8.546,
    "vote_count": 8555,
    "price": 7.99
  },
  {
    "adult": False,
    "backdrop_path": "/6oaL4DP75yABrd5EbC4H2zq5ghc.jpg",
    "genre_ids": [16, 10751, 14],
    "id": 129,
    "original_language": "ja",
    "original_title": "\u5343\u3068\u5343\u5c0b\u306e\u795e\u96a0\u3057",
    "overview": "A young girl, Chihiro, becomes trapped in a strange new world of spirits. When her parents undergo a mysterious transformation, she must call upon the courage she never knew she had to free her family.",
    "popularity": 126.829,
    "poster_path": "/39wmItIWsg5sZMyRUHLkWBcuVCM.jpg",
    "release_date": "2001-07-20",
    "title": "Spirited Away",
    "director": "Hayao Miyazaki",
    "main_actors": [
      "Rumi Hiiragi",
      "Miyu Irino",
      "Mari Natsuki",
      "Takeshi Naito",
      "Yasuko Sawaguchi"
    ],
    "genres": ["Animation", "Family", "Fantasy"],
    "runtime": 125,
    "video": False,
    "vote_average": 8.537,
    "vote_count": 16382,
    "price": 9.99
  },
  {
    "adult": False,
    "backdrop_path": "/90ez6ArvpO8bvpyIngBuwXOqJm5.jpg",
    "genre_ids": [35, 18, 10749],
    "id": 19404,
    "original_language": "hi",
    "original_title": "\u0926\u093f\u0932\u0935\u093e\u0932\u0947 \u0926\u0941\u0932\u094d\u0939\u0928\u093f\u092f\u093e \u0932\u0947 \u091c\u093e\u092f\u0947\u0902\u0917\u0947",
    "overview": "Raj is a rich, carefree, happy-go-lucky second generation NRI. Simran is the daughter of Chaudhary Baldev Singh, who in spite of being an NRI is very strict about adherence to Indian values. Simran has left for India to be married to her childhood fianc\u00e9. Raj leaves for India with a mission at his hands, to claim his lady love under the noses of her whole family. Thus begins a saga.",
    "popularity": 37.563,
    "poster_path": "/lfRkUr7DYdHldAqi3PwdQGBRBPM.jpg",
    "release_date": "1995-10-20",
    "title": "Dilwale Dulhania Le Jayenge",
    "director": "Aditya Chopra",
    "main_actors": [
      "Shah Rukh Khan",
      "Kajol",
      "Amrish Puri",
      "Farida Jalal",
      "Anupam Kher"
    ],
    "genres": ["Comedy", "Drama", "Romance"],
    "runtime": 190,
    "video": False,
    "vote_average": 8.529,
    "vote_count": 4429,
    "price": 11.99
  },
  {
    "adult": False,
    "backdrop_path": "/nMKdUUepR0i5zn0y1T4CsSB5chy.jpg",
    "genre_ids": [18, 28, 80, 53],
    "id": 155,
    "original_language": "en",
    "original_title": "The Dark Knight",
    "overview": "Batman raises the stakes in his war on crime. With the help of Lt. Jim Gordon and District Attorney Harvey Dent, Batman sets out to dismantle the remaining criminal organizations that plague the streets. The partnership proves to be effective, but they soon find themselves prey to a reign of chaos unleashed by a rising criminal mastermind known to the terrified citizens of Gotham as the Joker.",
    "popularity": 181.169,
    "poster_path": "/qJ2tW6WMUDux911r6m7haRef0WH.jpg",
    "release_date": "2008-07-16",
    "title": "The Dark Knight",
    "director": "Christopher Nolan",
    "main_actors": [
      "Christian Bale",
      "Heath Ledger",
      "Aaron Eckhart",
      "Michael Caine",
      "Maggie Gyllenhaal"
    ],
    "genres": ["Action", "Crime", "Drama", "Thriller"],
    "runtime": 152,
    "video": False,
    "vote_average": 8.515,
    "vote_count": 32672,
    "price": 10.99
  },
  {
    "adult": False,
    "backdrop_path": "/8eihUxjQsJ7WvGySkVMC0EwbPAD.jpg",
    "genre_ids": [35, 53, 18],
    "id": 496243,
    "original_language": "ko",
    "original_title": "\uae30\uc0dd\ucda9",
    "overview": "All unemployed, Ki-taek's family takes peculiar interest in the wealthy and glamorous Parks for their livelihood until they get entangled in an unexpected incident.",
    "popularity": 73.293,
    "poster_path": "/7IiTTgloJzvGI1TAYymCfbfl3vT.jpg",
    "release_date": "2019-05-30",
    "title": "Parasite",
    "director": "Bong Joon-ho",
    "main_actors": [
      "Song Kang-ho",
      "Lee Sun-kyun",
      "Cho Yeo-jeong",
      "Choi Woo-shik",
      "Park So-dam"
    ],
    "genres": ["Comedy", "Drama", "Thriller"],
    "runtime": 132,
    "video": False,
    "vote_average": 8.506,
    "vote_count": 18091,
    "price": 8.99
  },
  {
    "adult": False,
    "backdrop_path": "/vxJ08SvwomfKbpboCWynC3uqUg4.jpg",
    "genre_ids": [14, 18, 80],
    "id": 497,
    "original_language": "en",
    "original_title": "The Green Mile",
    "overview": "A supernatural tale set on death row in a Southern prison, where gentle giant John Coffey possesses the mysterious power to heal people's ailments. When the cell block's head guard, Paul Edgecomb, recognizes Coffey's miraculous gift, he tries desperately to help stave off the condemned man's execution.",
    "popularity": 66.337,
    "poster_path": "/8VG8fDNiy50H4FedGwdSVUPoaJe.jpg",
    "release_date": "1999-12-10",
    "title": "The Green Mile",
    "director": "Frank Darabont",
    "main_actors": [
      "Tom Hanks",
      "Michael Clarke Duncan",
      "David Morse",
      "Bonnie Hunt",
      "James Cromwell"
    ],
    "genres": ["Crime", "Drama", "Fantasy"],
    "runtime": 189,
    "video": False,
    "vote_average": 8.5,
    "vote_count": 17281,
    "price": 7.99
  },
  {
      "adult": False,
      "backdrop_path": "/suaEOtk1N1sgg2MTM7oZd2cfVp3.jpg",
      "genre_ids": [
          53,
          80
      ],
      "id": 680,
      "original_language": "en",
      "original_title": "Pulp Fiction",
      "overview": "A burger-loving hit man, his philosophical partner, a drug-addled gangster's moll and a washed-up boxer converge in this sprawling, comedic crime caper. Their adventures unfurl in three stories that ingeniously trip back and forth in time.",
      "popularity": 91.822,
      "poster_path": "/d5iIlFn5s0ImszYzBPb8JPIfbXD.jpg",
      "release_date": "1994-09-10",
      "title": "Pulp Fiction",
      "video": False,
      "vote_average": 8.5,
      "vote_count": 27719,
      "price": 9.99
  },
  {
      "adult": False,
      "backdrop_path": "/dIWwZW7dJJtqC6CgWzYkNVKIUm8.jpg",
      "genre_ids": [
          16,
          10749,
          18
      ],
      "id": 372058,
      "original_language": "ja",
      "original_title": "\u541b\u306e\u540d\u306f\u3002",
      "overview": "High schoolers Mitsuha and Taki are complete strangers living separate lives. But one night, they suddenly switch places. Mitsuha wakes up in Taki\u2019s body, and he in hers. This bizarre occurrence continues to happen randomly, and the two must adjust their lives around each other.",
      "popularity": 75.563,
      "poster_path": "/vfJFJPepRKapMd5G2ro7klIRysq.jpg",
      "release_date": "2016-08-26",
      "title": "Your Name.",
      "video": False,
      "vote_average": 8.486,
      "vote_count": 11282,
      "price": 11.99
  },
  {
      "adult": False,
      "backdrop_path": "/2u7zbn8EudG6kLlBzUYqP8RyFU4.jpg",
      "genre_ids": [
          12,
          14,
          28
      ],
      "id": 122,
      "original_language": "en",
      "original_title": "The Lord of the Rings: The Return of the King",
      "overview": "As armies mass for a final battle that will decide the fate of the world--and powerful, ancient forces of Light and Dark compete to determine the outcome--one member of the Fellowship of the Ring is revealed as the noble heir to the throne of the Kings of Men. Yet, the sole hope for triumph over evil lies with a brave hobbit, Frodo, who, accompanied by his loyal friend Sam and the hideous, wretched Gollum, ventures deep into the very dark heart of Mordor on his seemingly impossible quest to destroy the Ring of Power.\u200b",
      "popularity": 205.431,
      "poster_path": "/rCzpDGLbOoPwLjy3OAm5NUPOTrC.jpg",
      "release_date": "2003-12-17",
      "title": "The Lord of the Rings: The Return of the King",
      "video": False,
      "vote_average": 8.482,
      "vote_count": 24016,
      "price": 10.99
  },
  {
      "adult": False,
      "backdrop_path": "/ghgfzbEV7kbpbi1O8eIILKVXEA8.jpg",
      "genre_ids": [
          35,
          18,
          10749
      ],
      "id": 13,
      "original_language": "en",
      "original_title": "Forrest Gump",
      "overview": "A man with a low IQ has accomplished great things in his life and been present during significant historic events\u2014in each case, far exceeding what anyone imagined he could do. But despite all he has achieved, his one true love eludes him.",
      "popularity": 106.538,
      "poster_path": "/arw2vcBveWOVZr6pxd9XTd1TdQa.jpg",
      "release_date": "1994-06-23",
      "title": "Forrest Gump",
      "video": False,
      "vote_average": 8.472,
      "vote_count": 27249,
      "price": 8.99
  },
  {
      "adult": False,
      "backdrop_path": "/7TF4p86ZafnxFuNqWdhpHXFO244.jpg",
      "genre_ids": [
          18,
          80
      ],
      "id": 769,
      "original_language": "en",
      "original_title": "GoodFellas",
      "overview": "The true story of Henry Hill, a half-Irish, half-Sicilian Brooklyn kid who is adopted by neighbourhood gangsters at an early age and climbs the ranks of a Mafia family under the guidance of Jimmy Conway.",
      "popularity": 96.484,
      "poster_path": "/aKuFiU82s5ISJpGZp7YkIr3kCUd.jpg",
      "release_date": "1990-09-12",
      "title": "GoodFellas",
      "video": False,
      "vote_average": 8.5,
      "vote_count": 12764,
      "price": 7.99
  },
  {
      "adult": False,
      "backdrop_path": "/Adrip2Jqzw56KeuV2nAxucKMNXA.jpg",
      "genre_ids": [
          37
      ],
      "id": 429,
      "original_language": "it",
      "original_title": "Il buono, il brutto, il cattivo",
      "overview": "While the Civil War rages on between the Union and the Confederacy, three men \u2013 a quiet loner, a ruthless hitman, and a Mexican bandit \u2013 comb the American Southwest in search of a strongbox containing $200,000 in stolen gold.",
      "popularity": 70.751,
      "poster_path": "/bX2xnavhMYjWDoZp1VM6VnU1xwe.jpg",
      "release_date": "1966-12-22",
      "title": "The Good, the Bad and the Ugly",
      "video": False,
      "vote_average": 8.462,
      "vote_count": 8533,
      "price": 9.99
  },
  {
      "adult": False,
      "backdrop_path": "/sJNNMCc6B7KZIY3LH3JMYJJNH5j.jpg",
      "genre_ids": [
          28,
          18
      ],
      "id": 346,
      "original_language": "ja",
      "original_title": "\u4e03\u4eba\u306e\u4f8d",
      "overview": "A samurai answers a village's request for protection after he falls on hard times. The town needs protection from bandits, so the samurai gathers six others to help him teach the people how to defend themselves, and the villagers provide the soldiers with food.",
      "popularity": 39.49,
      "poster_path": "/8OKmBV5BUFzmozIC3pPWKHy17kx.jpg",
      "release_date": "1954-04-26",
      "title": "Seven Samurai",
      "video": False,
      "vote_average": 8.5,
      "vote_count": 3632,
      "price": 11.99
  },
  {
      "adult": False,
      "backdrop_path": "/gwj4R8Uy1GwejKqfofREKI9Jh7L.jpg",
      "genre_ids": [
          16,
          18,
          10752
      ],
      "id": 12477,
      "original_language": "ja",
      "original_title": "\u706b\u5782\u308b\u306e\u5893",
      "overview": "In the final months of World War II, 14-year-old Seita and his sister Setsuko are orphaned when their mother is killed during an air raid in Kobe, Japan. After a falling out with their aunt, they move into an abandoned bomb shelter. With no surviving relatives and their emergency rations depleted, Seita and Setsuko struggle to survive.",
      "popularity": 0.064,
      "poster_path": "/k9tv1rXZbOhH7eiCk378x61kNQ1.jpg",
      "release_date": "1988-04-16",
      "title": "Grave of the Fireflies",
      "video": False,
      "vote_average": 8.456,
      "vote_count": 5470,
      "price": 10.99
  },
  {
      "adult": False,
      "backdrop_path": "/7lyq8hK0MhPHpUXdnqbFvZYSfkk.jpg",
      "genre_ids": [
          18,
          10749
      ],
      "id": 11216,
      "original_language": "it",
      "original_title": "Nuovo Cinema Paradiso",
      "overview": "A filmmaker recalls his childhood, when he fell in love with the movies at his village's theater and formed a deep friendship with the theater's projectionist.",
      "popularity": 44.111,
      "poster_path": "/gCI2AeMV4IHSewhJkzsur5MEp6R.jpg",
      "release_date": "1988-11-17",
      "title": "Cinema Paradiso",
      "video": False,
      "vote_average": 8.45,
      "vote_count": 4325,
      "price": 8.99
  },
  {
      "adult": False,
      "backdrop_path": "/gavyCu1UaTaTNPsVaGXT6pe5u24.jpg",
      "genre_ids": [
          35,
          18
      ],
      "id": 637,
      "original_language": "it",
      "original_title": "La vita \u00e8 bella",
      "overview": "A touching story of an Italian book seller of Jewish ancestry who lives in his own little fairy tale. His creative and happy life would come to an abrupt halt when his entire family is deported to a concentration camp during World War II. While locked up he tries to convince his son that the whole thing is just a game.",
      "popularity": 61.57,
      "poster_path": "/74hLDKjD5aGYOotO6esUVaeISa2.jpg",
      "release_date": "1997-12-20",
      "title": "Life Is Beautiful",
      "video": False,
      "vote_average": 8.448,
      "vote_count": 12945,
      "price": 7.99
  },
  {
            "adult": False,
            "backdrop_path": "/9faGSFi5jam6pDWGNd0p8JcJgXQ.jpg",
            "genre_ids": [
                18,
                80
            ],
            "id": 1396,
            "origin_country": [
                "US"
            ],
            "original_language": "en",
            "original_name": "Breaking Bad",
            "overview": "Walter White, a New Mexico chemistry teacher, is diagnosed with Stage III cancer and given a prognosis of only two years left to live. He becomes filled with a sense of fearlessness and an unrelenting desire to secure his family's financial future at any cost as he enters the dangerous world of drugs and crime.",
            "popularity": 478.531,
            "poster_path": "/ztkUQFLlC19CCMYHW9o1zWhJRNq.jpg",
            "first_air_date": "2008-01-20",
            "name": "Breaking Bad",
            "vote_average": 8.915,
            "vote_count": 14282
        },
        {
            "adult": False,
            "backdrop_path": "/tuCU2yVRM2iZxFkpqlPUyvd6tSu.jpg",
            "genre_ids": [
                16,
                35,
                10765
            ],
            "id": 94954,
            "origin_country": [
                "US"
            ],
            "original_language": "en",
            "original_name": "Hazbin Hotel",
            "overview": "In attempt to find a non-violent alternative for reducing Hell's overpopulation, the daughter of Lucifer opens a rehabilitation hotel that offers a group of misfit demons a chance at redemption.",
            "popularity": 100.352,
            "poster_path": "/rXojaQcxVUubPLSrFV8PD4xdjrs.jpg",
            "first_air_date": "2024-01-18",
            "name": "Hazbin Hotel",
            "vote_average": 8.851,
            "vote_count": 1101
        },
        {
            "adult": False,
            "backdrop_path": "/96RT2A47UdzWlUfvIERFyBsLhL2.jpg",
            "genre_ids": [
                16,
                10759,
                10765
            ],
            "id": 209867,
            "origin_country": [
                "JP"
            ],
            "original_language": "ja",
            "original_name": "\u846c\u9001\u306e\u30d5\u30ea\u30fc\u30ec\u30f3",
            "overview": "After the party of heroes defeated the Demon King, they restored peace to the land and returned to lives of solitude. Generations pass, and the elven mage Frieren comes face to face with humanity\u2019s mortality. She takes on a new apprentice and promises to fulfill old friends\u2019 dying wishes. Can an elven mind make peace with the nature of life and death? Frieren embarks on her quest to find out.",
            "popularity": 141.388,
            "poster_path": "/dqZENchTd7lp5zht7BdlqM7RBhD.jpg",
            "first_air_date": "2023-09-29",
            "name": "Frieren: Beyond Journey's End",
            "vote_average": 8.834,
            "vote_count": 290
        },
        {
            "adult": False,
            "backdrop_path": "/wQEW3xLrQAThu1GvqpsKQyejrYS.jpg",
            "genre_ids": [
                16,
                10765,
                10759,
                9648
            ],
            "id": 94605,
            "origin_country": [
                "US"
            ],
            "original_language": "en",
            "original_name": "Arcane",
            "overview": "Amid the stark discord of twin cities Piltover and Zaun, two sisters fight on rival sides of a war between magic technologies and clashing convictions.",
            "popularity": 107.318,
            "poster_path": "/fqldf2t8ztc9aiwn3k6mlX3tvRT.jpg",
            "first_air_date": "2021-11-06",
            "name": "Arcane",
            "vote_average": 8.749,
            "vote_count": 4005
        },
        {
            "adult": False,
            "backdrop_path": "/kU98MbVVgi72wzceyrEbClZmMFe.jpg",
            "genre_ids": [
                16,
                10759,
                10765
            ],
            "id": 246,
            "origin_country": [
                "US"
            ],
            "original_language": "en",
            "original_name": "Avatar: The Last Airbender",
            "overview": "In a war-torn world of elemental magic, a young boy reawakens to undertake a dangerous mystic quest to fulfill his destiny as the Avatar, and bring peace to the world.",
            "popularity": 102.632,
            "poster_path": "/9jUuxbMSp3cwC2DDrSAs2F43Ric.jpg",
            "first_air_date": "2005-02-21",
            "name": "Avatar: The Last Airbender",
            "vote_average": 8.7,
            "vote_count": 4087
        },
        {
            "adult": False,
            "backdrop_path": "/a6ptrTUH1c5OdWanjyYtAkOuYD0.jpg",
            "genre_ids": [
                10759,
                35,
                16
            ],
            "id": 37854,
            "origin_country": [
                "JP"
            ],
            "original_language": "ja",
            "original_name": "\u30ef\u30f3\u30d4\u30fc\u30b9",
            "overview": "Years ago, the fearsome Pirate King, Gol D. Roger was executed leaving a huge pile of treasure and the famous \"One Piece\" behind. Whoever claims the \"One Piece\" will be named the new King of the Pirates.\n\nMonkey D. Luffy, a boy who consumed a \"Devil Fruit,\" decides to follow in the footsteps of his idol, the pirate Shanks, and find the One Piece. It helps, of course, that his body has the properties of rubber and that he's surrounded by a bevy of skilled fighters and thieves to help him along the way.\n\nLuffy will do anything to get the One Piece and become King of the Pirates!",
            "popularity": 133.568,
            "poster_path": "/cMD9Ygz11zjJzAovURpO75Qg7rT.jpg",
            "first_air_date": "1999-10-20",
            "name": "One Piece",
            "vote_average": 8.7,
            "vote_count": 4641
        },
        {
            "adult": False,
            "backdrop_path": "/rBF8wVQN8hTWHspVZBlI3h7HZJ.jpg",
            "genre_ids": [
                16,
                35,
                10765,
                10759
            ],
            "id": 60625,
            "origin_country": [
                "US"
            ],
            "original_language": "en",
            "original_name": "Rick and Morty",
            "overview": "Rick is a mentally-unbalanced but scientifically gifted old man who has recently reconnected with his family. He spends most of his time involving his young grandson Morty in dangerous, outlandish adventures throughout space and alternate universes. Compounded with Morty's already unstable family life, these events cause Morty much distress at home and school.",
            "popularity": 385.418,
            "poster_path": "/gdIrmf2DdY5mgN6ycVP0XlzKzbE.jpg",
            "first_air_date": "2013-12-02",
            "name": "Rick and Morty",
            "vote_average": 8.697,
            "vote_count": 9704
        },
        {
            "adult": False,
            "backdrop_path": "/A6tMQAo6t6eRFCPhsrShmxZLqFB.jpg",
            "genre_ids": [
                10759,
                16,
                10765,
                35
            ],
            "id": 31911,
            "origin_country": [
                "JP"
            ],
            "original_language": "ja",
            "original_name": "\u92fc\u306e\u932c\u91d1\u8853\u5e2b FULLMETAL ALCHEMIST",
            "overview": "Disregard for alchemy\u2019s laws ripped half of Edward Elric\u2019s limbs from his body and left his brother Alphonse\u2019s soul clinging to a suit of armor. To restore what was lost, the brothers seek the Philosopher\u2019s Stone. Enemies and allies \u2013 the corrupt military, the Homunculi, and foreign alchemists \u2013 will alter the Elric brothers course, but their purpose will remain unchanged and their bond unbreakable.",
            "popularity": 166.821,
            "poster_path": "/8H4ej2NpujYVBPsW2smmzC8d2xU.jpg",
            "first_air_date": "2009-04-05",
            "name": "Fullmetal Alchemist: Brotherhood",
            "vote_average": 8.7,
            "vote_count": 2032
        },
        {
            "adult": False,
            "backdrop_path": "/hPea3Qy5Gd6z4kJLUruBbwAH8Rm.jpg",
            "genre_ids": [
                80,
                18
            ],
            "id": 60059,
            "origin_country": [
                "US"
            ],
            "original_language": "en",
            "original_name": "Better Call Saul",
            "overview": "Six years before Saul Goodman meets Walter White. We meet him when the man who will become Saul Goodman is known as Jimmy McGill, a small-time lawyer searching for his destiny, and, more immediately, hustling to make ends meet. Working alongside, and, often, against Jimmy, is \u201cfixer\u201d Mike Ehrmantraut. The series tracks Jimmy\u2019s transformation into Saul Goodman, the man who puts \u201ccriminal\u201d in \u201ccriminal lawyer\".",
            "popularity": 250.579,
            "poster_path": "/fC2HDm5t0kHl7mTm7jxMR31b7by.jpg",
            "first_air_date": "2015-02-08",
            "name": "Better Call Saul",
            "vote_average": 8.688,
            "vote_count": 5169
        },
        {
            "adult": False,
            "backdrop_path": "/900tHlUYUkp7Ol04XFSoAaEIXcT.jpg",
            "genre_ids": [
                18
            ],
            "id": 87108,
            "origin_country": [
                "US"
            ],
            "original_language": "en",
            "original_name": "Chernobyl",
            "overview": "The true story of one of the worst man-made catastrophes in history: the catastrophic nuclear accident at Chernobyl. A tale of the brave men and women who sacrificed to save Europe from unimaginable disaster.",
            "popularity": 86.683,
            "poster_path": "/hlLXt2tOPT6RRnjiUmoxyG1LTFi.jpg",
            "first_air_date": "2019-05-06",
            "name": "Chernobyl",
            "vote_average": 8.7,
            "vote_count": 6255
        },
        {
            "adult": False,
            "backdrop_path": "/70YdbMELM4b8x8VXjlubymb2bQ0.jpg",
            "genre_ids": [
                18,
                10751
            ],
            "id": 70785,
            "origin_country": [
                "CA"
            ],
            "original_language": "en",
            "original_name": "Anne with an E",
            "overview": "A coming-of-age story about an outsider who, against all odds and numerous challenges, fights for love and acceptance and for her place in the world. The series centers on a young orphaned girl in the late 1890\u2019s, who, after an abusive childhood spent in orphanages and the homes of strangers, is mistakenly sent to live with an elderly woman and her aging brother. Over time, 13-year-old Anne will transform their lives and eventually the small town in which they live with her unique spirit, fierce intellect and brilliant imagination.",
            "popularity": 99.966,
            "poster_path": "/6P6tXhjT5tK3qOXzxF9OMLlG7iz.jpg",
            "first_air_date": "2017-03-19",
            "name": "Anne with an E",
            "vote_average": 8.7,
            "vote_count": 4630
        },
        {
            "adult": False,
            "backdrop_path": "/cHyY5z4txdVyGtYMvBJhCqCcJso.jpg",
            "genre_ids": [
                16,
                10765,
                18,
                10759,
                35,
                10762
            ],
            "id": 92685,
            "origin_country": [
                "US"
            ],
            "original_language": "en",
            "original_name": "The Owl House",
            "overview": "An animated fantasy-comedy series that follows Luz, a self-assured teenage girl who accidentally stumbles upon a portal to a magical world where she befriends a rebellious witch, Eda, and an adorably tiny warrior, King. Despite not having magical abilities, Luz pursues her dream of becoming a witch by serving as Eda's apprentice at the Owl House and ultimately finds a new family in an unlikely setting.",
            "popularity": 108.445,
            "poster_path": "/zhdy3PcNVE15wj1wrxn45ARZBnx.jpg",
            "first_air_date": "2020-01-10",
            "name": "The Owl House",
            "vote_average": 8.665,
            "vote_count": 1578
        },
        {
            "adult": False,
            "backdrop_path": "/xdTwlG8MYAOkFuAGUqt8LgmgTNZ.jpg",
            "genre_ids": [
                16,
                35,
                10765
            ],
            "id": 62741,
            "origin_country": [
                "JP"
            ],
            "original_language": "ja",
            "original_name": "\u795e\u69d8\u306f\u3058\u3081\u307e\u3057\u305f",
            "overview": "Nanami was just a normal high school girl down on her luck until a stranger\u2019s lips marked her as the new Land God and turned her world upside down. Now, she\u2019s figuring out the duties of a deity with the help of Tomoe, a reformed fox demon who reluctantly becomes her familiar in a contract sealed with a kiss. The new responsibilities\u2014and boys\u2014are a lot to handle, like the crow demon masquerading as a gorgeous pop idol and the adorable snake spirit who\u2019s chosen the newly minted god to be his bride. As the headstrong Tomoe tries to whip her into shape, Nanami finds that love just might have cute, pointed fox ears. With romance in the air, will the human deity be able to prove herself worthy of her new title?",
            "popularity": 60.764,
            "poster_path": "/5E7GL8KxpFemEFl3Lv8Fu4RuSwa.jpg",
            "first_air_date": "2012-10-02",
            "name": "Kamisama Kiss",
            "vote_average": 8.7,
            "vote_count": 885
        },
        {
            "adult": False,
            "backdrop_path": "/3GQKYh6Trm8pxd2AypovoYQf4Ay.jpg",
            "genre_ids": [
                16,
                10759,
                10765
            ],
            "id": 85937,
            "origin_country": [
                "JP"
            ],
            "original_language": "ja",
            "original_name": "\u9b3c\u6ec5\u306e\u5203",
            "overview": "It is the Taisho Period in Japan. Tanjiro, a kindhearted boy who sells charcoal for a living, finds his family slaughtered by a demon. To make matters worse, his younger sister Nezuko, the sole survivor, has been transformed into a demon herself. Though devastated by this grim reality, Tanjiro resolves to become a \u201cdemon slayer\u201d so that he can turn his sister back into a human, and kill the demon that massacred his family.",
            "popularity": 98.148,
            "poster_path": "/xUfRZu2mi8jH6SzQEJGP6tjBuYj.jpg",
            "first_air_date": "2019-04-06",
            "name": "Demon Slayer: Kimetsu no Yaiba",
            "vote_average": 8.658,
            "vote_count": 6409
        },
        {
            "adult": False,
            "backdrop_path": "/rqbCbjB19amtOtFQbb3K2lgm2zv.jpg",
            "genre_ids": [
                16,
                10765,
                10759
            ],
            "id": 1429,
            "origin_country": [
                "JP"
            ],
            "original_language": "ja",
            "original_name": "\u9032\u6483\u306e\u5de8\u4eba",
            "overview": "Many years ago, the last remnants of humanity were forced to retreat behind the towering walls of a fortified city to escape the massive, man-eating Titans that roamed the land outside their fortress. Only the heroic members of the Scouting Legion dared to stray beyond the safety of the walls \u2013 but even those brave warriors seldom returned alive. Those within the city clung to the illusion of a peaceful existence until the day that dream was shattered, and their slim chance at survival was reduced to one horrifying choice: kill \u2013 or be devoured!",
            "popularity": 127.928,
            "poster_path": "/hTP1DtLGFamjfu8WqjnuQdP1n4i.jpg",
            "first_air_date": "2013-04-07",
            "name": "Attack on Titan",
            "vote_average": 8.7,
            "vote_count": 6346
        },
        {
            "adult": False,
            "backdrop_path": "/2w8FaLwwJTWr6ExUMeVgT2Th5YT.jpg",
            "genre_ids": [
                16,
                35,
                18,
                10759
            ],
            "id": 42705,
            "origin_country": [
                "JP"
            ],
            "original_language": "ja",
            "original_name": "\u306f\u3058\u3081\u306e\u4e00\u6b69",
            "overview": "Makunouchi Ippo is an ordinary high school student in Japan. Since he spends most of his time away from school helping his mother run the family business, he doesn't get to enjoy his younger years like most teenagers. Always a target for bullying at school (the family fishing business grants him a distinct odor), Ippo's life is one of hardship. One of these after-school bullying sessions turns Ippo's life around for the better, as he is saved by a boxer named Takamura. He decides to follow in Takamura's footsteps and train to become a boxer, giving his life direction and purpose. Ippo's path to perfecting his pugilistic prowess is just beginning...",
            "popularity": 200.373,
            "poster_path": "/qC4taY6yB9BWJ8IxcbnXR8yUS4o.jpg",
            "first_air_date": "2000-10-03",
            "name": "Fighting Spirit",
            "vote_average": 8.654,
            "vote_count": 1044
        },
        {
            "adult": False,
            "backdrop_path": "/3MC8VIxq8u1vKOKTfz6FtrFXuMZ.jpg",
            "genre_ids": [
                10765,
                18,
                10759,
                9648
            ],
            "id": 135157,
            "origin_country": [
                "KR"
            ],
            "original_language": "ko",
            "original_name": "\ud658\ud63c",
            "overview": "A powerful sorceress in a blind woman's body encounters a man from a prestigious family, who wants her help to change his destiny.",
            "popularity": 131.772,
            "poster_path": "/q2IiPRSXPOZ6qVRj36WRAYEQyHs.jpg",
            "first_air_date": "2022-06-18",
            "name": "Alchemy of Souls",
            "vote_average": 8.65,
            "vote_count": 579
        },
        {
            "adult": False,
            "backdrop_path": "/7BoRhg8zXP0ca9Zql4p8llCFR2P.jpg",
            "genre_ids": [
                18,
                10765,
                35
            ],
            "id": 221851,
            "origin_country": [
                "KR"
            ],
            "original_language": "ko",
            "original_name": "\ub0b4 \ub0a8\ud3b8\uacfc \uacb0\ud63c\ud574\uc918",
            "overview": "Kang Ji-won, a terminally ill cancer patient, is killed by her husband and best friend after she witnesses them having an affair. She wakes up 10 years before the incident and decides to seek revenge with the help of Yu Ji-hyuk, a director at the company where she works. Now, she must reclaim her fate and eliminate the trash from her life.",
            "popularity": 102.858,
            "poster_path": "/y2hvE76S6Me0uhYEQ1P8lGf7Wm0.jpg",
            "first_air_date": "2024-01-01",
            "name": "Marry My Husband",
            "vote_average": 8.648,
            "vote_count": 423
        },
        {
            "adult": False,
            "backdrop_path": "/j0viazcPT7Te2XC7iomH9lBtiVG.jpg",
            "genre_ids": [
                35,
                18
            ],
            "id": 68349,
            "origin_country": [
                "KR"
            ],
            "original_language": "ko",
            "original_name": "\uc5ed\ub3c4\uc694\uc815 \uae40\ubcf5\uc8fc",
            "overview": "A competitive swimmer crosses paths with his childhood friend, a rising weight lifting star, and realizes that she has a secret crush on his cousin.",
            "popularity": 53.907,
            "poster_path": "/kyZKEtDNBS5S3ZobqJssdhUYUfv.jpg",
            "first_air_date": "2016-11-16",
            "name": "Weightlifting Fairy Kim Bok-joo",
            "vote_average": 8.6,
            "vote_count": 804
        },
        {
            "adult": False,
            "backdrop_path": "/dfmPbyeZZSz3bekeESvMJaH91gS.jpg",
            "genre_ids": [
                16,
                10765,
                10759,
                18
            ],
            "id": 95557,
            "origin_country": [
                "US"
            ],
            "original_language": "en",
            "original_name": "INVINCIBLE",
            "overview": "Mark Grayson is a normal teenager except for the fact that his father is the most powerful superhero on the planet. Shortly after his seventeenth birthday, Mark begins to develop powers of his own and enters into his father\u2019s tutelage.",
            "popularity": 100.123,
            "poster_path": "/dMOpdkrDC5dQxqNydgKxXjBKyAc.jpg",
            "first_air_date": "2021-03-25",
            "name": "INVINCIBLE",
            "vote_average": 8.6,
            "vote_count": 4424
        }
]


@bp.route('/')
def index():
  return render_template('index.html', movies=movies)

@bp.route('/detail/<int:dvdid>')
def detail(dvdid):
  
  for item in dvd:
    print(item)
    if item['id'] == dvdid:
      result = item
      
  return render_template('detail.html', dvd=result)

@bp.route('/movies_all')
def get_movies_all():
  return render_template('movies_all.html', movies=movies)

@bp.route('/series_all')
def get_series_all():
  return render_template('series_all.html', tv_series=tv_series)