# import library
import webbrowser
import fresh_tomatoes

# create movie class
class Movie():
    #VALID_RATING = ["C", "D","HD"]
    # a function that takes movie_title, a short movie_storieline, a front fost and a small trailer
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        # define title
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)





