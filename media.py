import webbrowser

class Movie():
    """This class provides a way to store movie related information"""
    
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    def __init__(self, movie_title, storyline, poster_image, trailer_youtube):
        """Initializes the instance variables
        movie_title     -> a string of the movie's title
        year_of_release -> an integer corresponding to year of release of the movie
        poster_image    -> a string of movie's poster image URL
        trailer_youtube -> a string of movie's trailer URL on youtube"""

        self.title = movie_title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Opens trailer in a webbrowser"""
        webbrowser.open(self.trailer_youtube_url)
