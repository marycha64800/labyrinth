#!/bin/env python3faire de a sau
# -*- coding: utf-8 -*-

""" Module qui se charge d'envoyer les fichier """

import os
import pickle



class FileManager:
    """ Cette classe s'occupe de d'aller chercher les fichier que l'on a besoin """


    def load_map(self, target):
        """
        """
        with open(target, "r") as file:
            return file.read()
