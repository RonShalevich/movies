import movies
import fresh_tomatoes

toy_story = movies.Movie("Toy Story",
                         "A story of a boy and his toys",
                         "https://goo.gl/images/h95syN",
                         "https://www.youtube.com/watch?v=KYz2wyBy3kc")
# print (toy_story.storyline)

avatar = movies.Movie("Avatar",
                      "A marine on an alien planet",
                      "https://goo.gl/images/EJ7mBN",
                      "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
# print(avatar.storyline)
# avatar.show_trailer()

movies = [toy_story, avatar]
fresh_tomatoes.open_movies_page(movies)
