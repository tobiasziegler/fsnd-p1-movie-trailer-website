'''Script to produce a movies website. It generates a page displaying a range
of movies titles and posters, with playable video trailers when the user
selects a movie.'''

import media
import fresh_tomatoes

# Deadpool
deadpool = media.Movie(
    "Deadpool",
    "https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg",
    "https://www.youtube.com/watch?v=FyKWUTwSYAs")

# Moneyball
moneyball = media.Movie(
    "Moneyball",
    "https://upload.wikimedia.org/wikipedia/en/2/2e/Moneyball_Poster.jpg",
    "https://www.youtube.com/watch?v=-4QPVo0UIzc")

# The Social Network
social_network = media.Movie(
    "The Social Network",
    "https://upload.wikimedia.org/wikipedia/en/7/7a/Social_network_film_poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=lB95KLmpLR4")

# Blade Runner 2049
blade_runner_2049 = media.Movie(
    "Blade Runner 2049",
    "https://upload.wikimedia.org/wikipedia/en/2/27/Blade_Runner_2049_logo.png",  # noqa
    "https://www.youtube.com/watch?v=gCcx85zbxz4")

# Iron Man
iron_man = media.Movie(
    "Iron Man",
    "https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG",
    "https://www.youtube.com/watch?v=8hYlB38asDY")

# Tron: Legacy
tron_legacy = media.Movie(
    "Tron: Legacy",
    "https://upload.wikimedia.org/wikipedia/en/c/c2/Tron_Legacy_poster.jpg",
    "https://www.youtube.com/watch?v=L9szn1QQfas")

movies = [deadpool, moneyball, social_network, blade_runner_2049, iron_man,
          tron_legacy]

fresh_tomatoes.open_movies_page(movies)
