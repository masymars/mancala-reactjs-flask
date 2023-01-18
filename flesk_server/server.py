# Import flask and datetime module for showing date and time
from flask import Flask
from flask import current_app,jsonify,request
import datetime
from MancalaBoard import  MancalaBoard
from Game import  Game
from Play import  Play  

from flask_cors import CORS, cross_origin


bord1 = {"A": 4, "B": 4, "C": 4, "D": 4, "E": 4, "F": 4, "1": 0, "G": 4, "H": 4, "I": 4, "J": 4, "K": 4, "L": 4,"2": 0}
boards = MancalaBoard(bord1)
game = Game(boards,1)
pl = Play(game)

turn = pl.game.playerSide


x = datetime.datetime.now()
  




# Initializing flask app
app = Flask(__name__)
CORS(app, support_credentials=True)
  
@app.route('/restart')
def restart():
    bord1 = {"A": 4, "B": 4, "C": 4, "D": 4, "E": 4, "F": 4, "1": 0, "G": 4, "H": 4, "I": 4, "J": 4, "K": 4, "L": 4,"2": 0}
    boards = MancalaBoard(bord1)
    game = Game(boards,1)
    pl1 = Play(game)
    pl.game=pl1.game
    print(bord1)
    return  [False]



@cross_origin(supports_credentials=True)
@app.route("/do", methods=["POST"], strict_slashes=False)
def do_move():
    print("hi")
    print(request.json["move"])
    t = pl.humanTurn(request.json['move'])


    
    return [ pl.game.state.bord, t]
  
@app.route("/doc", methods=["POST"], strict_slashes=False)
def do_comp():
    print("hi comp")
   
    t = pl.computerTurn()
    

    
    return [pl.game.state.bord,t]
  

@app.route("/getbord", methods=["POST"], strict_slashes=False)
def do_comp11():
    print("hi bord")
   
   
    

    
    return [pl.game.state.bord,t]
  






# Route for seeing a data
@app.route('/data')
def get_time():
    
    # Returning an api for showing in  reactjs
    return pl.game.state.bord
  
@app.route('/gameover')
def get_go():
    
    # Returning an api for showing in  reactjs
    return  [pl.game.gameOver() ]
@app.route('/pmove')
def get_go2():
    
    # Returning an api for showing in  reactjs
    return  [pl.game.state.possibleMoves(1)]

@app.route('/findwiner')
def findwiners():
    print("winner is", pl.game.findWinner() )
    # Returning an api for showing in  reactjs
    return  [pl.game.findWinner() ]

""""""






# Running app
if __name__ == '__main__':
    app.run(debug=True)