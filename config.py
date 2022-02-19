import pygame
import tkinter as tk


# global variables
# get a window that is always 75% of window
map_width = 50
map_height = 10
tile_size = 25

width, height = int(tk.Tk().winfo_screenwidth() * .75), int(tk.Tk().winfo_screenheight() * .75)
print(width, height)
width -= width % tile_size
height -= height % tile_size
size = width, height

print(width, height)
screen = pygame.display.set_mode(size)
colors = {"black": [0, 0, 0], "green": [0, 255, 0], "red": [255, 0, 0], "blue":[0,0,255], "yellow":[255, 255, 0], "pink":[255, 192, 203], "white":[255,255,255]}
all_sprites = pygame.sprite.Group()
bullet_sprites = pygame.sprite.Group()
item_sprites = pygame.sprite.Group()
map_sprites = pygame.sprite.Group()



with open("test_map.txt", 'w') as f:

    temp = [[" " for _ in range(width//tile_size)] for _ in range(height//tile_size)]
    temp[0] = ["x" for _ in range(width//tile_size)]
    temp[-1] = ["x" for _ in range(width//tile_size)]
    for _ in temp:
        _[0] = "x"
        _[-1] = "x"

    for _ in temp:
        f.write("".join(_))
        f.write("\n")
    test_map = temp

with open("map1.txt") as f:
    temp = f.readlines()
    world_map = [[_ for _ in temp[i].strip("\n")] for i in range(len(temp))]
    for _ in world_map:
        print(_)