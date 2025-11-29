This project is a simple web-based cricket scoreboard system built using:

HTML/CSS – for creating the user interface

Flask (server.py) – for backend logic and routing

HTTP requests – to send data between the website and the server


The main goal was to create a functional webpage where users can enter and view cricket scores in a structured and user-friendly way.




2. How the Website Works

The project contains three important files:

a) index.html

This is the homepage of the website.
It displays basic information and acts as the starting point before going to the actual scoreboard page.
It contains:

Navigation or button to go to “Start” page

Simple UI designed using HTML


b) start.html

This is the main scoreboard interface.
Users can:

Enter team names

Add runs, wickets, overs

Submit the score


This page sends the data to the backend (server.py) using a POST request when the user clicks submit.

c) server.py

This is the backend file created using Flask.
It connects HTML pages to the backend and handles:

Routing (which page opens when a user clicks a link)

Receiving scoreboard data from HTML forms

Processing data and sending it back to HTML for display


Flask acts like the manager that connects everything together.


3. What is Flask & Why We Used It

Flask is a lightweight Python web framework used to create backend servers easily.

We used Flask because:

It is simple to set up

Works smoothly with HTML files

Handles form submissions

Lets us run a local web server on our laptop


Flask makes sure that:

When user opens the website → correct HTML file loads

When user submits form → data is received at /submit route

After processing → result is displayed on new HTML page

4. How Frontend and Backend Communicate

When the user enters data on start.html, the form sends information to the backend like this:

1. User fills the cricket score form


2. Form sends data using

method="POST" action="/submit"


3. server.py receives this data using:

request.form['team_name']


4. Backend processes the received values


5. Backend sends back a response (rendering another HTML template or showing updated score)



This cycle creates a complete functional system.


5. Role of server.py in Combining Everything

server.py is the central backbone of the project.

It does 4 important jobs:

1. Runs the local server


2. Loads HTML templates using

render_template()


3. Receives and processes user input


4. Sends the processed output back to UI



server.py = connects frontend UI + backend logic + data flow


6. Final Project Flow (Step-by-Step)

1. User opens website → Flask serves index.html


2. User clicks Start → Flask serves start.html


3. User fills the scoreboard form


4. Form sends data to Flask server


5. Flask processes data


6. Updated score/confirmation is displayed


7. The system behaves like a real backend-powered scoreboard

7. Conclusion

The project successfully demonstrates:

Website development using HTML

Backend development using Flask

Complete frontend-backend integration

Handling user input and rendering output

Real-time scoreboard logic


This small system represents how modern web applications work internally using routing, templates, and server-side processing.
