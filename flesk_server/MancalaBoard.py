
import math
class MancalaBoard:
  bord = {"A": 4, "B": 16, "C": 4, "D": 4, "E": 4, "F": 4, "1": 0, "G": 4, "H": 4, "I": 4, "J": 4, "K": 4, "L": 4,"2": 0}
  def __init__(self,bord):
    self.bord = bord
  def possibleMoves(self,player) :
      tp = []
      nb=0
      for key, value in self.bord.items():
         nb=nb+1
         if player == 1 and nb<=6:
           if value != 0 and key != "1" and key != "2":
               tp.append(key)
         if player == 2 and nb>6 and nb<=13:
           if value != 0 and key != "2"and key != "1" :
               tp.append(key)


      return tp



  def doMove(self ,f):
     # Make a copy of the board to prevent modifying the original dictionary
     print(f)
     
     # Find the starting position and the number of stones to distribute
     start = f
     stones = self.bord[start]
     self.bord[start] = 0
     p =[]
     i=0
     t=0
     for key, value in self.bord.items():
         p.append(value)
         
         if key==start:
           t=i
         i+=1  
     # Distribute the stones to the other pits
     i = 1

     while stones > 0:
        pit = (t + i) % len(p)
        i += 1
        if  t <6 and pit != 13:
             p[pit] += 1
             stones -= 1
              
        if  t >6 and pit != 6:  
             p[pit] += 1
             stones -= 1
             
     if p[pit]==1:
           print(t)
           print(t)
           print(t)
           print(t)
           temp = p[12-pit]
           p[12-pit] =0
           if  t <6:
             p[6] = p[6]+temp
           else :   
             p[13] = p[13]+temp
            
     i = 0   
     for key, value in self.bord.items():
         self.bord[key]   = p[i]  
         i += 1  


     
     if t <6 and pit ==6:
        return 1
     if t >6 and pit ==13:
        return 2
     if t <6 :
        return 2
     else: 
        return 1         