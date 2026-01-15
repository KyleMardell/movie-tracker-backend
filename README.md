# My Movie Tracker App

[Live App](https://movietracker.kylemardell.me/)

[Front End Repo](https://github.com/KyleMardell/movie-tracker-frontend)

My movie tracker is exactly that, a movie tracker. Add movies to a list and mark them as watched, track movies you want to watch or have watched. Bonus, it tells you where you can stream, buy or rent them un the U.K.

The movie tracker was inspired by my wife who hasn't seen many movies and we would forget what to watch, when we finally get time to watch a movie. Finding out where you can stream the movie was inspired by a work colleague when talking about the original idea and really gives the app more of a reason to use it.

I built the app using a Django REST framework back end API with a Postgres database, with the front end using Next.js, React and Bootstrap.
The API has basic auth with username and password requirements, although I have not imposed any username or password restrictions and they can be any string not using spaces or white space. When signing up or logging in JSON web tokens are sent back to the user and saved in local storage. When the user logs out the refresh and access tokens are simply deleted. 
The only database model other than the default django user model is a movie model. The movie model saves the movie name, TMDB ID number, poster image path, date added, watched status and associated user. This basic movie information is all that is needed to display the users movies and mark them as watched. The back end uses a django list, create, edit and delete default view, and a custom watched status view that only changes watched from true to false and visa versa.

The app uses TMDB - The Movie Database's API for all movie information, posters and watch providers.
The front end uses Next.js and React, creating custom hooks and page components such as movie cards, carousel and details page. The carousel was made with usability in mind, creating a custom scroll component to track when a user drags the carousel left or right and highlighting a selected movie to avoid false movie selection. 

When designing the app, I used excalidraw to make some basic wire frames and planned the database model fields before planning the build. I wrote a simple list to plan the app build, I have shown a basic version below.
- Back end set up
    - Create repo
    - Set up a new Django project and app
    - Install Rest framework and Django auth
    - Add model
    - Create serializer, view and urls
    - Create Postgres database
    - Deploy app to VPS
    - Link database and set up superuser
    - Test back end, remove default view once tested
- Front end set up
    - Create repo
    - Set up a new Next.js app
    - Install Bootstrap
    - Create login page and basic home page
    - Link login to API and confirm tokens
    - Create movie card
    - Create carousel
    - Create movie detail page/modal
    - Set up TMDB API call
    - Display TMDB movie lists
    - Create add to list function
    - Create delete from list function
    - Update add to list button to remove button
    - Create watched status button and function
    - Create users movie context
    - Display users movie list
    - Set up user sign up/registration
    - Auto log in new users
    - Add sign up feedback
    - Add error feedback
    - Add search movie page

When I was creating the front end, I stayed flexible in the build and added tasks when I came to that part, first building out the basic auth and log in, displaying a basic logged in home page. Once I had the log in auth working, I then worked on the TMDB API, working out the calls I needed to make, the data returned and how to display it. 

This was also my first time creating a project using Typescript, which I admit was a challenge. I had learned about Typescript types, how to create custom types and their general uses, however having not used it in a project before, I initially struggled with types on all functions and variables. Initially I used the "any" type to get thing working before writing hard types for things such as movie data in different formats throughout the front end. I tested the use of common custom types that could be used over the entire app and in hindsight I would also plan my types in the same manor as my database models as I could have created a re-usable movie type if I had planned ahead. Again as this was my first time using Typescript I learned a lot in this project about how to use it, and planning ahead when using custom types.

Another challenge was setting up the app in my VPS. I use CapRover which is an open source platform as a service that sets up apps using docker. I have used CapRover on my VPS for almost a year at this point and it has taught me a lot about hosting, deployment and general DevOps practices. I learned some basic Docker use and how to deploy the back end in a Docker container, as well as connecting to the docker app through SSH and the VPS to set up my superuser on the Django back end. When deploying both the back end and front end apps I had to deal with multiple bugs including working out how to enter the Docker container and set up my superuser as mentioned. I also had a bug where I had used a Next.js function of useSearchParams to read a components parameters which was causing me issues in deployment. In the end I removed the use of this Next.js function and read the params using URLSearchParams instead. I thought about using a context when trying to fix the bug as it was due to a welcome message when a new user signs up, being sent to the dashboard via component params. However this felt like overkill to confirm a one time message, and using URLSearchParams worked in the end. 

The only bug I have come across post deployment is when a user enters a space in their username as I have only done basic username and password checks during sign up auth. This is because although I needed auth for user accounts and user lists, auth was no the main focus of what I wanted to learn with this project, which was setting up my first full stack app, post boot camp, and learning to use typescript. Both of which I am happy with what I achieved, as well as having a functions movie tracker app.

I wont be updating this app or adding any further features as I wanted it to be simple and easy to use, with the main function of a user movie list and where to find the movies. 

If you want to check out the app, the link is above. Go sign up, check out some movies, add some to your list and find out where you can stream them. 