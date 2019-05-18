#!/bin/env python3
# -*- coding: utf-8 -*-

""" Module de la classe display qui se charge de rendre jolis les information a l'ecran pour la partie menu """

import os

class DisplayMenu:


    def __init__(self):

        self.menu_with_save = {

            "0" : ("file_menu/home_with_save", False),
            "01" : ("save/autosave", True),
            "02" : ("file_menu/choice_level", False),
            "03" : ("file_menu/scores", False),
            "04" : ("file_menu/rules", False),
            "021": ("file_menu/level_easy", False),
            "022": ("file_menu/level_hard", False),
            "023": ("file_menu/level_very_hard",False),
            "0211":("level/lvl_easy/map1.txt",True),
            "0212":("level/lvl_easy/map2.txt",True),


        }

        self.menu_whithout_save = {

            "0": ("file_menu/home", False),
            "01": ("file_menu/choice_level", False),
            "02": ("file_menu/scores", False),
            "03": ("file_menu/rules", False),
            "011": ("file_menu/level_easy", False),
            "012": ("file_menu/level_hard", False),
            "013": ("file_menu/level_very_hard", False),
            "0111": ("level/lvl_easy/map1.txt", True),
            "0112": ("level/lvl_easy/map2.txt", True),

        }



    def home(self):
        """ Module charge le bon ecran accceuil en fonction de l'existance de la sauvegarde et
            adapte le menu en consequence
        """

        target = None
        while target is None:
            if os.path.exists("save/autosave"):
                target = self.navigation_menu(self.menu_with_save)

            else:
                target =self.navigation_menu(self.menu_whithout_save)


        return target


    def navigation_menu(self, paths_menu, path_choice="0"):
        """
            Metode qui recupere un dictionire et une cle par defaut 0 qui est le menu de depart
            une fonction recursive se charge des erreurs de saisies

            le dictionaire a en valeur un tuple les chemins qui peuvents etre une page de menu aurons un false
            comme qualificatif et les chemin qui sont les cartes auront un True comme qualificatif

            la clef s'incemente au fur et a mesure des choix de l'utilisateur

        """
        try:
            target, final_target = paths_menu[path_choice]

            while final_target is not True:


                with open(target, "r") as files:
                    print (files.read())

                choice = str(input("Choix: "))

                if choice != "0":
                    path_choice += choice
                else:
                    path_choice = path_choice[:-1]

                if path_choice == "":
                    return exit()


                target, final_target = paths_menu[path_choice]


            return target

        except KeyError:
            path_choice = path_choice[:-1]
            return self.navigation_menu(paths_menu=paths_menu, path_choice=path_choice)






