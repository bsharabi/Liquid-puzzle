from api.IAlgo import IAlgo
from api.lib import *

class Algo(IAlgo):
    
    
    def __init__(self) -> None:
        pass
     
    

    def generate_tubes(self,empty_tube:int=1) -> list[int,list[list]]:
        tubes_number = rd.randint(2, 8)
        tubes_colors = []
        available_colors = []
        for i in range(tubes_number):
            tubes_colors.append([])
            if i < tubes_number - empty_tube:
                for j in range(4):
                    available_colors.append(i)
        for i in range(tubes_number - empty_tube):
            for j in range(4):
                color = rd.choice(available_colors)
                tubes_colors[i].append(color)
                available_colors.remove(color)

        return tubes_number, tubes_colors

    def generate_tubes(self,full:int,size:int,colors:int,empty_tube:int=1) -> list[int,list[list]]:
        
        
        tubes_colors = []
        available_colors = []
        for i in range(size):
            tubes_colors.append([])
            for j in range(colors):
                available_colors.append(i)
        for i in range(size):
            for j in range(colors):
                color = rd.choice(available_colors)
                tubes_colors[i].append(color)
                available_colors.remove(color)
        for i in range(empty_tube):
            tubes_colors.append([])
        return  tubes_colors


