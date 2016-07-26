import webbrowser

#Parent class to Movie & TvShow
class Video():
    def __init__(self, title,duration):
        self.title = title
        self.duration = duration



# This class provides a way to store movie related information
class Movie(Video):
    """This class connects with entertainment_center.py. 
        The Imdb class connects with the Imdb.com  
    """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    def __init__(self,
                 title,
                 duration,
                 movie_storyline,
                 poster_image,
                 trailer_youtube):
        # Video.__init__(self,title,duration)
        # super() isnt working and I have been googling to find out why. I am so stumped on it. Would love feed back! :)
        self.storyline = movie_storyline
        super(Movie, self).__init__(title, duration) 
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
    

class TvShow(Video):

    def __init__(self,
                 title,
                 duration,
                 season,
                 episode, tv_station):
        # Video.__init__(self,title,duration)
        super(Movie, self).__init__(title, duration)
        self.season = season
        self.episode = episode
        self.tv_station = tv_station
        
