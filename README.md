# Movie-trailer-website
A simple movie trailer website that lists out my favourites movies alongwith their trailers. The project uses a class Movie in **Python** to generate static web pages which contains links to their trailer on youtube.

## Demo
For a demo, checkout <http:>

## Documentation
### Class Movie
The Movie object class consists of four class variables, a constructor method and a class method for playing Movie object's movie trailer. The code is located in [media.py]().

#### contructor method
The class Movie consits of a constructor which is called when an object of the class is created and it takes in four parameters- [title](#movietitle), [storyline](#storyline), [poster_image_url](#movieposter_image_url), and [trailer_youtube_url](#movietrailer_youtube_url).

##### movie.title
it is a string to identify title of the movie object.

##### movie.storyline
it is a string containing summary of the plot of the movie.

##### movie.poster_image_url
it is a string of URL of the poster of the movie

##### movie.trailer_youtube_url
it is a string of URL of the movie's trailer on youtube

#### show_trailer method
this method takes in the youtube URL of any object of class Movie and plays their traileron youtube.

### Movie trailer 
