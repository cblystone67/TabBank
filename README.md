# TabBank
## TabBank is a Django-based web application that allows users to store and organize guitar tabs and related information. It provides a user-friendly interface for managing tabs, searching for new tabs, and collaborating with others.

### Installation
* Copy code
* git clone <https://github.com/cblystone67/TabBank>
* pip install -r requirements.txt
* python manage.py migrate
* python manage.py runserver

## Features
* The application has the the ability to login and logout users.
* The ability to allow a user his/hers own access to the website.
* The ability to search and save songs form a dedicated API
* The ability to save comments to each individual song.

## Usage
* The user will be allowed full CRUD ability.
* The user can create new new songs
* The user can view those songs and the details of those songs
* The user can update and edit those songs and comments
* The user can delete songs and comments.

* When the user lands on the page they are met with the Home Page.
![Screenshot](main_app/static/images/HomePage.png)
This page allows the user to either signup and create a new account or sign in if they are a current user.
On this page the user can either use the navigation bar to sign in or up or they can utilize the links on the welcome card.
After siging in they are awarded their own page welcoming them: 
![Screenshot](main_app/static/images/Logged%20In.png)
Upon landing on this page they now can take advantage of the application and start utilizing the features.
- First if they are a current user their page will load with the current songs they have saved.
- Second they then have several options: 
* first is to click on the current song which will give them the details of the song: 
![Screenshot](main_app/static/images/DetailsPage.png)
 - This page gives them the details of the song:
 * They can edit the song information:
 * Delete the song:
 * Create a comment: Which will appear on the page with the information entered.
 * They then can either edit that comment or delete that comment as they see fit.

## The Search
- As the user they can decide to search for an individual song from an API called Songsterr.
* By entering either the Artist Name or Song title they will be returned with a list of songs.
![Screenshot](main_app/static/images/SearchPage.png)

- Upon the user submitting the search they are then given the results page:
![Screenshot](main_app/static/images/ResultsPage.png)







## API Integration
* API used: <https://publicapis.io/songsterr-music-api>
Icebox Challenges





