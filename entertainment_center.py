import media
import fresh_tomatoes

"""
declaration of favorite movies  with 4 arguments:
title
storyline
poster URL
trailer URL
"""

forrest_gump = media.Movie("Forrest Gump",
                           "Forrest Gump, a man with a low I.Q., joins the army for service where he meets Dan and Bubba. However, he cannot stop thinking about his childhood sweetheart Jenny Curran, whose life is messed up.",
                           "http://t0.gstatic.com/images?q=tbn:ANd9GcSppDgk99BKVA4TJtWc1FN4-HUkdWrFNfMm1-M0nQ01sIOcbTZu",
                        "https://www.youtube.com/watch?v=DRc7JrORPas")

good_will_hunting = media.Movie("Good Will Hunting",
                     "storyling",
                     "http://t0.gstatic.com/images?q=tbn:ANd9GcT4vHOLWBM56R6fNs7K9xcEf7V8M8mzrzi6LtWGXrqfg8-KynGn",
                     "https://www.youtube.com/watch?v=PaZVjZEFkRs")

avengers_infinity_war = media.Movie("Avengers Infinity War",
                                    "Iron Man, Thor, the Hulk and the rest of the Avengers unite to battle their most powerful enemy yet -- the evil Thanos. On a mission to collect all six Infinity Stones, Thanos plans to use the artifacts to inflict his twisted will on reality. The fate of the planet and existence itself has never been more uncertain as everything the Avengers have fought for has led up to this moment.",
                                    "https://upload.wikimedia.org/wikipedia/en/4/4d/Avengers_Infinity_War_poster.jpg",
                                    "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

the_imitation_game = media.Movie("The Imitation Game", "Storyline",
                             "http://t0.gstatic.com/images?q=tbn:ANd9GcQQ5vi9xgRkP0nk5aRn8tcGEGRnOQyM-aAS1ldqfQSi_69V1yfU",
                             "https://www.youtube.com/watch?v=nuPZUUED5uk")

schindlers_list = media.Movie("Schindler's List", "storyline",
                                "https://upload.wikimedia.org/wikipedia/en/3/38/Schindler%27s_List_movie.jpg",
                                "https://www.youtube.com/watch?v=gG22XNhtnoY")

shawshank_redemption = media.Movie("Shawshank Redemption", "Storyline",
                           "http://t0.gstatic.com/images?q=tbn:ANd9GcSkmMH-bEDUS2TmK8amBqgIMgrfzN1_mImChPuMrunA1XjNTSKm",
                           "https://www.youtube.com/watch?v=6hB3S9bIaco")

#assign individual movies to movie list
movies = [forrest_gump, good_will_hunting, avengers_infinity_war,
          the_imitation_game, shawshank_redemption, schindlers_list]

#call movie trailer page method and movies list
fresh_tomatoes.open_movies_page(movies)

