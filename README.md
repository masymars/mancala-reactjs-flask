# mancala-reactjs-flask
Mancala is a board game that we built using React.js for the frontend and Flask
Mancala is a board game that is traditionally played with small stones or beads. A React.js frontend can be used to build the user interface for the game, 
while a Flask backend can be used to implement the game logic, including the Minimax algorithm for the AI player. 
The Minimax algorithm is a decision-making algorithm that is commonly used in two-player games such as Mancala. It works by evaluating all possible moves that can be made by the AI player and the opponent, 
and choosing the move that will lead to the best outcome for the AI player while minimizing the opponent's potential gain. 

This algorithm is implemented by recursively evaluating the game tree and assigning a score to each possible move, based on the outcome of the game.

To run the client side , you will need to have Node.js and npm (Node Package Manager) installed on your computer. 
Once you have those set up, you can follow these steps:

Open a terminal and navigate to the root directory of your React.js project.

Run the command npm install to install all the necessary dependencies for the project.

Run the command npm start to start the development server. This will automatically launch the application in your default web browser at http://localhost:3000.


To install Flask, you will need to have Python installed on your computer. Once you have Python set up, you can follow these steps:

Open a terminal and run the command pip install flask to install Flask. This will install the latest version of Flask and its dependencies.

To start a Flask server, you will need to have a file named "server.py" or similar that contain the flask code. Once you have that file, you can follow these steps:

Open a terminal and navigate to the root directory of your Flask project.

Run the command export FLASK_APP=server.py to set the environment variable for the Flask application.

Run the command flask run to start the development server. This will start the server and make the application accessible at http://localhost:5000

You can now make changes to the code and the changes will be reflected in the browser automatically
