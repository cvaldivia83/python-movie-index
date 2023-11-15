


### CS50 Final Project

# MovieIndex

#### Video Demo:

[Youtube CS50P's presentation video](https://youtu.be/OsDiAIGcTg0)

#### Description:

In my final project I will implement a program where the user can favorite his favorite movies. The user can:

- List his favorite movies

- Add a movie to his bookmarks

- Remove a movie from bookmarks

- Mark a movie as seen

- Give a rating to each movie - (1-5) stars

- Look for a movie on the internet and add it to its bookmarks

- Save a movie in a CSV file

- Remove a movie from a CSV file

- Generate a PDF file with all bookmarked movies listed


To accomplish this task I will be following a MVC pattern (model, view, controller) and **single-responsibility principle** (**SRP**)


Each file contains a unique class. And each class performs only one task.

1. Movie:

This will be the model. It will be responsible for generating instances of movies.

Each instance of movie must contain: title, description, rating and seen parameters.

2. Database:

This class will work as a database for this project. Its sole task is to save movies, delete movies, update movies.

2. Controller

The controller will handle the inputs from the user and pass it to the model.

3. View

The view will only print data to the user and collect the user's answers.

4. Router

Router will create routes to perform the actions the user would like to do in the app

5. App

This class will be responsible for initializing our Python App.

6. CSV

It will be a file that will work as a database. It will save the movies the user adds in the cookbook.

For each one of those classes I will also implement tests. All tests can be located inside the ```/test``` folder
