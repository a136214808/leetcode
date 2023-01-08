'''
874. Walking Robot Simulation

A robot on an infinite XY-plane starts at point (0, 0) facing north.
'''
from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x,y =0,0#position
        dx,dy =0,1#direction
        result =0 # store value
        obstacles = set(map(tuple,obstacles))#list - > map

        for command in commands:
            if command == -1: #right
                dx,dy = dy,-dx
            elif command == -2:
                dx,dy = -dy,dx
            elif 1<=command<=9:
                for _ in range(command):
                    if (x+dx,y+dy) in obstacles:
                        break
                    x +=dx
                    y +=dy
                result = max(result,x**2+y**2)
            return result