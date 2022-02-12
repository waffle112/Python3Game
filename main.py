import pygame, sys
from game_classes import *
import tkinter as tk
import config

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



def generate_level(map):
    for y in range(0, len(map)):
        for x in range(0, len(map[y])):
            if map[y][x] == "x":
                temp = wall(x * config.tile_size, y * config.tile_size)
                config.all_sprites.add(temp)
            #elif symbol if keyword for a picture
                #load in a picture
            else:
                pass



# game function
def game():
    clock = pygame.time.Clock()

    #start main menu?
    mainMenu()
    config.screen.fill(config.colors["black"])

    main_player = Player(config.size)
    main_player.set_pos(config.width / 2, config.height / 2)

    config.all_sprites.add(main_player)

    #test enemy
    enemy1 = enemy_1()
    config.all_sprites.add(enemy1)

    #test item
    item1 = item()
    config.all_sprites.add(item1)
    config.item_sprites.add(item1)

    set_text("test")

    generate_level(config.world_map)

    while True:
        clock.tick(60)  # set fps to 60

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        # update
        config.all_sprites.update()
        config.item_sprites.update(main_player)


        # check collision



        # display game
        config.screen.fill(config.colors["black"])
        config.all_sprites.draw(config.screen)

        pygame.display.flip()


# if name
if __name__ == "__main__":

    game()
