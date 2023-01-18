import copy

from MancalaBoard import  MancalaBoard
from Game import  Game

from math import inf

class Play():
    bord1 = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "1": 16, "G": 4, "H": 4, "I": 4, "J": 4, "K": 4, "L": 4,
             "2": 0}
    boards = MancalaBoard(bord1)
    game =Game(boards,0)
    def __init__(self, game):
        self.game = game
    def humanTurn(self,move):
      t = 1
     

      if move in self.game.state.possibleMoves(self.game.playerSide) :
             t = self.game.state.doMove(move)
             print(t)
             print(self.game.state.bord)
      return t

    def computerTurn(self):
      
        self.game.state.possibleMoves(self.game.playerSide)
        child_game = copy.deepcopy(self.game)
        bestValue, bestPit = self.minimax(child_game,5, False,alpha = -inf, beta= inf )
        print("move",bestPit)
        print(self.game.state.possibleMoves(2))
        print(self.game.state.bord)
        if bestPit in self.game.state.possibleMoves(2):

            t = self.game.state.doMove(bestPit)
            print(t)
            
        return(t)


    def minimax(self, game , depth, maximizingPlayer, alpha, beta):
        if depth == 0 or game.gameOver():
            bestValue = game.evaluate1()
            bestPit = None


            return bestValue, bestPit
        children = game.childern()

        if maximizingPlayer:
            bestPit = None
            bestValue = -inf
            for child in children:
                value,pit  = self.minimax(child[0], depth - 1, False, alpha, beta)
                if value > bestValue:
                    bestPit = child[1]
                bestValue = max(bestValue, value)
                alpha = max(alpha, bestValue)
                if beta <= alpha:
                    bestPit = child[1]
                    break


            return bestValue,bestPit
        else:
            bestValue = inf
            bestPit = None
            for child in children:
                value,pit = self.minimax(child[0], depth - 1, True, alpha, beta)
                if value < bestValue:
                    bestPit = child[1]
                bestValue = min(bestValue, value)
                beta = min(beta, bestValue)

                if beta <= alpha:

                    break

            return bestValue,bestPit


        
    def NegaMaxAlphaBetaPruning(self,game1,player, depth, alpha, beta):


        if game1.gameOver()  or depth == 1 :

            bestValue = game1.evaluate()
            bestPit = None
            if player == game1.playerSide :

             bestValue = - bestValue

            return bestValue, bestPit

        bestValue = -inf
        bestPit = None


        for pit in game1.state.possibleMoves(player):
         if pit == "1" or pit == "2":
          print(pit + "-----errrrrrrrrrrrrrr")
         else :


          child_game = copy.copy(game1)
          t = child_game.state.doMove(pit)


          value, _ = self.NegaMaxAlphaBetaPruning(child_game, t, depth - 1, -beta, -alpha)

          if value > bestValue :
              bestValue = value
              bestPit = pit

          if bestValue > alpha :

            alpha = bestValue

          if beta <= alpha :
            break

        return bestValue, bestPit