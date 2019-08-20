import fresh_tomatoes
import media
#Tile , Storyline, Poster, trailer
toy_story = media.Movie("toy story", "Animated movie","https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=wmiIUN-7qhE")

# print(toy_story.storyline)
#for avatar = init funtion get call

avatar = media.Movie("Avatar", "story of aliens", "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY&t=1s" )

taken_3 = media.Movie("Taken 3", "It is all about kidnapping girls", "https://upload.wikimedia.org/wikipedia/en/6/6f/Taken_3_poster.jpg", "https://www.youtube.com/watch?v=HUJZjUaNzgw&t=6s")
# print(avatar.storyline)

twelve_angry_men = media.Movie("twelve angry men","A very old movie about judges", "https://upload.wikimedia.org/wikipedia/en/9/91/12_angry_men.jpg", "https://www.youtube.com/watch?v=J61XJhYiUpg")

#another instance to create a movie
Gotti = media.Movie("Gotti", "is an American biographical crime film", "https://upload.wikimedia.org/wikipedia/en/7/79/Gotti_movie_poster.jpg", "https://www.youtube.com/watch?v=Y3V5uy5Qo94")

# fast_eight = media.Movie("fast_eight", "car Racing", "")

#avatar.show_trailer()
movies= [toy_story, avatar, taken_3, twelve_angry_men, Gotti]

fresh_tomatoes.open_movies_page(movies)



# print(media.Movie.__doc__)
# print(media.Movie.VALID_RATING)
#in media making a class "Movie"
#In entertainment defining instances
#when create instance of a class like story, the class constractor get call
#this is essentially the init method inside the class
#It is here that all of the data that we initialize that is associated with instance
#the constractor uses the keyword seld or instance in qestion
#all of the variable associated with instance called instance variable and unique to an object and can be accessed by
#using the self keyword inside the class
# for the file fresh tomatoes, it has function inside called "open_movies_page" this funtion receive a list of movies
# and creates and opens in HTML file or webpage that showcases those movies



