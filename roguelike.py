import pygame, sys
from rgame_classes import *
import tkinter as tk
import config
import pickle
import gc


def gen_map(mapList, pics):
    for y in range(0, len(mapList)):
        for x in range(0, len(mapList[y])):
            if mapList[y][x] == "x":
                temp = wall(x * config.tile_size, y * config.tile_size, "white")
                config.all_sprites.add(temp)
                config.map_sprites.add(temp)
            #elif symbol if keyword for a picture
            #load in a picture from list pics
            else:
                pass


def checkWall(newMap, pos):
    #check total walls
    dir = [(0,1), (1,0), (-1,0), (0,-1)]
    total = 0
    for d in dir:
        newX, newY = pos[0] + d[0], pos[1] + d[1]
        if len(newMap[0]) > newX >= 0 and len(newMap) > newY >= 0 and newMap[newY][newX] == 'x':
            total += 1
    return total

#maze generator - DP version
def gen_random_map(width, height):
    newMap = [['x' for _ in range(width)] for _ in range(height)]
    randDir = [(0,1), (1,0), (-1,0), (0,-1)]
    toVisit = [[1,1]]
    visited = [[False for _ in range(width)] for _ in range(height)]

    while toVisit:
        oriPos = x, y = toVisit.pop()
        if checkWall(newMap, oriPos) >= 3:
            newMap[y][x] = ' '
            visited[y][x] = True
            random.shuffle(randDir)
            for d in randDir:
                nx, ny = d
                newPos = newX, newY = x + nx, y + ny
                if checkWall(newMap, newPos) == 3 and not visited[newY][newX]:
                    toVisit.append(newPos)
        #print(toVisit)

    for _ in newMap:
        print(_)
    input()

def game():
    player = Player(config.size)
    config.all_sprites.add(player)
    player.set_pos(config.tile_size * (config.width//2//config.tile_size), config.tile_size * (config.width//2//config.tile_size))
    clock = pygame.time.Clock()
    #m = gen_random_map(config.width // config.tile_size, config.height // config.tile_size)
    m = gen_random_map(10, 10)
    gen_map(config.world_map, [])
    while True:
        clock.tick(60)  # set fps to 60

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                keystate = pygame.key.get_pressed()
                # print(keystate)
                player.handle_movement(keystate)
                break


        # update
        config.all_sprites.update()


        # display game
        config.screen.fill(config.colors["black"])

        config.all_sprites.draw(config.screen)

        pygame.display.flip()
    pass


if __name__ == "__main__":
    game()