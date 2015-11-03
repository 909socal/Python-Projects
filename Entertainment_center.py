import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys who come to life",
                        "http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v7_ab.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print (toy_story.storyline)
#toy_story.show_trailer()

avatar = media.Movie("Avatar",
                     "A Marine on a alien plante",
                     "http://ia.media-imdb.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_SX640_SY720_.jpg",
                     "https://www.youtube.com/watch?v=EPTHpG7ovak")
#print (avatar.storyline)

fast_furious = media.Movie("Fast and Furious 7",
                            "A family who loves cars and friends",
                            "http://t1.gstatic.com/images?q=tbn:ANd9GcReedjA2vJSO4_6GDpsI3PShvbRqfAAEv03qaJ9qOxtiLZX0Jx7",
                            "https://www.youtube.com/watch?v=Skpu5HaVkOc")
#fast_furious.show_trailer()
movies = [toy_story,avatar,fast_furious]
fresh_tomatoes.open_movies_page(movies)
