import webbrowser


class Movie():
    """ The class Movie() has contains all the attributes """
    """ required to define and create a movie object"""
    def __init__(self, movie_title, movie_storyline,
                 poster_image,
                 trailer_youtube):
        """ the init function sets all the instance variables """
        """ to the parameters passed when an object is created """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ The show_trailer function plays the trailer """
        """ of the movie on a browser when it is called """
        webbrowser.open(self.trailer_youtube)
