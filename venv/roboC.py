#!/bin/env python3
# -*- coding: utf-8 -*-

import management_data
import labyrinth_controller
import menu
import user_input
import elements_of_game




def launch_game():


    game_menu = menu.DisplayMenu()
    game_data = management_data.FileManager()
    request_user = user_input.UserInput()



    robot = elements_of_game.Robot(name_robot=request_user.get_name())

    target = game_menu.home()

    labyrinth = labyrinth_controller.LabyrinthControl(game_data.load_map(target))

    robot.coordinates = labyrinth.robot_search()
    print (robot.coordinates)
    print (labyrinth)




launch_game()