#!/bin/env python3
# -*- coding: utf-8 -*-

from elements_of_game import LabyrinthElements, Robot

class LabyrinthControl(LabyrinthElements):

    """ """



    def __init__(self, laby):
        LabyrinthElements.__init__(self)


        self.labyrinth = laby.split("\n")


    def robot_search(self):

        for i in range(len(self.labyrinth)):
            if self.robot_picture in self.labyrinth[i]:
                return i , self.labyrinth[i].find(self.robot_picture)

    def __repr__(self):

        return "\n".join(self.labyrinth)
