#!/bin/env python3faire de a sau
# -*- coding: utf-8 -*-

"""Module de classe qui sert a recupere de facon securiser les entre de l'utilisateur """

class UserInput:

    def __init__(self):

        self.__up = "z"
        self.__left = "d"
        self.__right = "q"
        self.__down = "s"


    def get_name(self):

         user_name = str(input("Quel est votre nom/pseudo")).capitalize()

         if 1 > len(user_name) > 8:
             print ("Merci d'incrire un nom/pseudo entre 1 et 8 caractere")
             return self.get_name()
         elif user_name.isalnum() is False:
             print ("Merci de ne pas mettre d'espace ou de carectere speciaux")
             return self.get_name()

         return user_name









