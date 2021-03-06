# Movie-trailer-website
A simple movie trailer website that lists out my favourites movies alongwith their trailers. The project uses a class Movie in **Python** to generate static web pages which contains links to their trailer on youtube.

## Download
The files for the project may be [downloaded here](https://github.com/indranarayan12/ud036_StarterCode/archive/master.zip).
To see the project 
1. unzip the downloaded file and open fresh_tomatoes.html file or 
2. Install Python->
   Clone the project to your local environment->
   Open a shell interface and move to the project directory->
   Execute entertainment_center.py.
The website is now displayed on your default web browser.

## Documentation
### Class Movie
The Movie object class consists of four class variables, a constructor method and a class method for playing Movie object's movie trailer. The code is located in [media.py](https://github.com/indranarayan12/ud036_StarterCode/blob/master/media.py).

#### contructor method
The class Movie consits of a constructor which is called when an object of the class is created and it takes in four parameters- [title](#movietitle), [storyline](#moviestoryline), [poster_image_url](#movieposter_image_url), and [trailer_youtube_url](#movietrailer_youtube_url).

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

### Movie specifications
The favorite movies have been described in [entertainment_center.py](https://github.com/indranarayan12/ud036_StarterCode/blob/master/entertainment_center.py). [media.py](https://github.com/indranarayan12/ud036_StarterCode/blob/master/media.py) and [fresh_tomatoes.py](https://github.com/indranarayan12/ud036_StarterCode/blob/master/fresh_tomatoes.py) is imported and it calls a function open_movie_page of fresh_tomatoes.py which takes in a list of objects of the class Movie and opens it in the default window of the the machine for HTML files.
