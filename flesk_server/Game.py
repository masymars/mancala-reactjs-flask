
import math
from MancalaBoard import  MancalaBoard
import copy



class Game:
    bord={}
    state = MancalaBoard(bord)
    playerSide =0

    def __init__(self,state,playerSide):
         self.state = state
         self.playerSide =playerSide


    def gameOver(self) :
          if self.state.bord["A"] == 0 and  self.state.bord["B"] == 0 and  self.state.bord["C"] == 0 and  self.state.bord["D"] == 0 and  self.state.bord["E"] == 0 and  self.state.bord["F"] == 0 :
              self.state.bord["2"] = self.state.bord["G"] + self.state.bord["H"] + self.state.bord["I"] + self.state.bord["J"] + self.state.bord["K"] + self.state.bord["L"]
              self.state.bord["G"] =0
              self.state.bord["H"] =0
              self.state.bord["I"] = 0
              self.state.bord["J"] = 0
              self.state.bord["K"] = 0
              self.state.bord["L"] = 0
              return True
          if self.state.bord["G"]==0 and  self.state.bord["H"]==0 and  self.state.bord["I"] ==0 and  self.state.bord["J"]==0 and  self.state.bord["K"]==0 and  self.state.bord["L"]==0 :
              self.state.bord["1"] = self.state.bord["A"] + self.state.bord["B"] + self.state.bord["C"] + self.state.bord["D"] + self.state.bord["E"] + self.state.bord["F"]
              self.state.bord["A"] =0
              self.state.bord["B"] =0
              self.state.bord["C"] = 0
              self.state.bord["D"] = 0
              self.state.bord["E"] = 0
              self.state.bord["F"] = 0
              return True

          return False

    def findWinner(self):
        if self.state.bord["2"] < self.state.bord["1"] :
            return 1
        else :
            return 2


    def evaluate(self):
        return (self.state.bord["1"] - self.state.bord["2"])
    def evaluate1(self):
        # Calculate the number of stones in each pit and the mancalas
        pits = []
        for key, value in self.state.bord.items():
            pits.append(value)
       
    
        # Calculate the total number of stones for each player
        player1_stones = sum(pits[:7]) 
        player2_stones = sum(pits[7:])
    
        # Calculate the number of empty pits for each player
        player1_empty = sum(1 for pit in pits[:6] if pit == 0)
        player2_empty = sum(1 for pit in pits[6:] if pit == 0)
    
        # Calculate the score using a weighted combination of the number of stones, empty pits, and mancala stones
        player1_score = player1_stones + 2 * player1_empty + 4 * pits[6]
        player2_score = player2_stones + 2 * player2_empty + 4 * pits[13]
    
        return player1_score - player2_score
    def childern(self):
        M = self.state.possibleMoves(2)
        children = []
        for m in M:
            tp = copy.deepcopy(self)
            tp.state.doMove(m)

            children.append((tp, m))

        return children