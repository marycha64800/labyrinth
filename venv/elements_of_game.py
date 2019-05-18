#!/bin/env python3
# -*- coding: utf-8 -*-

""" module de la classe elements du jeu .

 Labyrinth elements defini les interation de tout les elements qui se trouve dans le labyrinte

 Roboc class fille de LabyrintheElments et defini les caracterisque du robot



"""

class LabyrinthElements:

    """ La class labyrinte defini les interation possible sous forme de tuple
    (objet, interation)
    False = on pu pas interagir
    True = on peu
    valeur = destructible valeur etant les point de defense
    None = Arrivée

    """


    def __init__(self):

        self.elements = {

            "O" : (False ,self.wall),
            "P" : (True, self.door),
            "U" : (True, self.upstairs),
            "E" : (True, self.way_out),
            "D" : (True, self.downstairs),

        }

        self.robot_picture = 'R'



    def wall(self):
        print ("Bangg!!")

    def door(self):
        print ("Gniii...plock!!")

    def upstairs(self):
        pass

    def way_out(self):
        pass
    def downstairs(self):
        pass



class Robot:

    """
    Reprend les attibut de LabyrinthElements et defini les fonction du robot

    """

    def __init__(self, name_robot):
        """

        :type name_robot: name user
        """
        self.coordinates = []
        self.name_robot = name_robot





