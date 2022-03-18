import pygame, sys
from game_classes import *
import tkinter as tk
import config
import pickle
import gc
'''
TODO
Eric - Make a Title Screen with buttons and menus - Done 
    restart screen? 
    props - interactable 
    walk around - random encounters 
    
    
Abraham - Make a boss mob
    Walls - 
'''




def mainMenu():
    quitButton = button(config.colors["black"], config.width//2-100, config.height//4, 100, 50, "Quit Game")
    startButton = button(config.colors["black"], config.width//2-100, config.height//4 - 100, 100, 50, "Start Game")

    start = False

    while True:
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quitButton.inBoundaries(pos):
                    pygame.quit()
                    quit()
                if startButton.inBoundaries(pos):
                    start = True
                    break
        if start:
            break

        quitButton.draw(config.screen, (255, 255, 255))
        startButton.draw(config.screen, (255, 255, 255))
        pygame.display.update()



def generate_level(map, pics):
    for y in range(0, len(map)):
        for x in range(0, len(map[y])):
            if map[y][x] == "x":
                temp = wall(x * config.tile_size, y * config.tile_size, "white")
                config.all_sprites.add(temp)
                config.map_sprites.add(temp)
            #elif symbol if keyword for a picture
                #load in a picture from list pics
            else:
                pass


# game function
def game():

    try:
        autosave = open("save.dat", "rb")
        game_state = pickle.load(autosave)
        print(game_state)
        #test player
        main_player = Player(config.size)
        main_player.rect = game_state["main_player.rect"]

        #test enemy
        enemy1 = enemy_1()
        enemy1.rect = game_state["enemy1.rect"]

        #test item
        item1 = item()
        item1.rect = game_state["item1.rect"]
        autosave.close()

    except IOError:
        #test player
        main_player = Player(config.size)
        main_player.set_pos(config.width / 2, config.height / 2)

        #test enemy
        enemy1 = enemy_1()

        #test item
        item1 = item()
    autosave = open("save.dat", "wb")

    clock = pygame.time.Clock()
    config.all_sprites.add(main_player)
    config.all_sprites.add(enemy1)
    config.all_sprites.add(item1)
    config.item_sprites.add(item1)
    #load in relevant info
    game_state = dict()


    #start main menu?
    mainMenu()
    config.screen.fill(config.colors["black"])

    set_text(["test1", "Test2", "Test3"])

    pics = []
    generate_level(config.world_map, pics)




    while True:
        clock.tick(60)  # set fps to 60

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_state["main_player.rect"]= main_player.rect
                game_state["enemy1.rect"] = enemy1.rect
                game_state["item1.rect"] = item1.rect
                pickle.dump(game_state, autosave, protocol=2)
                autosave.close()
                sys.exit()
            if event.type == pygame.USEREVENT+1: #custom event #1
                #reset buff action
                main_player.spreadshot = False
                pass


        # update
        config.all_sprites.update()
        config.item_sprites.update(main_player)



        # display game
        config.screen.fill(config.colors["black"])
        config.all_sprites.draw(config.screen)

        pygame.display.flip()


# if name
if __name__ == "__main__":

    game()
