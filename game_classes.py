import pygame
import config
import math
import random

pygame.font.init()
font_name = pygame.font.match_font('arial')


class Player(pygame.sprite.Sprite):
    # attributes/variables

    # init
    def __init__(self, size):
        # call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # [load] image or generate image
        self.image = pygame.Surface([30, 30])
        self.image.fill(config.colors["green"])

        # initialize rect/hitbox
        self.rect = self.image.get_rect()

        # handle movement variables
        self.x_spd, self.x_curr_spd = 5, 0
        self.y_spd, self.y_curr_spd = 5, 0

        # handle misc variables such as a bullet list/ammo count
        self.screen_width, self.screen_height = size
        self.bullet_speed = 10

    # update - mandatory
    def update(self):
        self.handle_movement()
        self.handle_mouse()
        pass

    # handle_movement
    def handle_movement(self):
        # reset speed
        self.x_curr_spd = 0
        self.y_curr_spd = 0

        # get key
        keystate = pygame.key.get_pressed()
        # print(keystate)
        if keystate[pygame.K_UP] or keystate[pygame.K_w]:
            self.y_curr_spd -= self.y_spd
            # self.image.fill(colors["green"]) # set self.image to a diff image instead
        elif keystate[pygame.K_DOWN] or keystate[pygame.K_s]:
            self.y_curr_spd += self.y_spd
            # self.image.fill(colors["pink"])
        elif keystate[pygame.K_LEFT] or keystate[pygame.K_a]:
            self.x_curr_spd -= self.x_spd
            # self.image.fill(colors["yellow"])
        elif keystate[pygame.K_RIGHT] or keystate[pygame.K_d]:
            self.x_curr_spd += self.x_spd
            # self.image.fill(colors["blue"])

        # update rect
        self.rect.x += self.x_curr_spd
        self.rect.y += self.y_curr_spd

        # boundaries check
        if self.rect.right >= self.screen_width:
            self.rect.right = self.screen_width
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= self.screen_height:
            self.rect.bottom = self.screen_height

    def handle_mouse(self):
        # check if left click
        mousestate = pygame.mouse.get_pressed()
        if mousestate[0]:
            print("left click")
            m_x, m_y = pygame.mouse.get_pos()
            p_x, p_y = self.get_pos()
            angle = math.atan2((m_y - p_y), (m_x - p_x))
            # make a bullet where the speed_x and speed_y = base_speed * math.cos(angle), base_speed * math.sin(angle)
            b = Bullet(p_x, p_y, self.bullet_speed, math.cos(angle), math.sin(angle))
            config.bullet_sprites.add(b)
            config.all_sprites.add(b)

    # handle_collision
    def handle_collision(self):
        pass

    # handle_sprite
    def handle_sprite(self):
        pass

    # shoot
    def shoot(self):
        pass

    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def get_pos(self):
        return self.rect.centerx, self.rect.centery


# add relevant classes to specific files i'll say
# like add bullets/ powerups into the class that will use them
class Bullet(pygame.sprite.Sprite):
    # attributes/variables
    # init
    def __init__(self, x, y, base_speed, speed_x, speed_y):
        # call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # load image or generate image
        self.image = pygame.Surface([5, 5])
        self.image.fill(config.colors["red"])

        # initialize rect/hitbox
        self.rect = self.image.get_rect()

        # handle misc variables
        self.rect.centerx = x
        self.rect.centery = y
        self.base_speed = base_speed
        self.speed_x = base_speed * speed_x
        self.speed_y = base_speed * speed_y

    # update - mandatory
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

class wall(pygame.sprite.Sprite):
    def __init__(self, x , y):
        # call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # [load] image or generate image
        self.image = pygame.Surface([config.tile_size, config.tile_size])
        self.image.fill(config.colors["white"])

        # initialize rect/hitbox
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class enemy_1(pygame.sprite.Sprite):

    def __init__(self):
        # call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # [load] image or generate image
        self.image = pygame.Surface([50, 50])
        self.image.fill(config.colors["pink"])

        # initialize rect/hitbox
        self.rect = self.image.get_rect()

        # random spawn
        self.rect.x = random.randint(0, config.width)
        self.rect.y = random.randint(0, config.height)

        # handle movement variables
        self.x_spd, self.x_curr_spd = 5, 0
        self.y_spd, self.y_curr_spd = 5, 0

        # initialize shooting setup
        self.shootlast = pygame.time.get_ticks()
        self.movelast = pygame.time.get_ticks()
        self.shootcooldown = 900
        self.mvcooldown = 200
        self.speed = 5

    def update(self):
        # behaviour of enemy
        # random movement
        # timer var that times the shooting speed
        # shoot in a ring?

        now = pygame.time.get_ticks()
        if now - self.shootlast >= self.shootcooldown:
            self.shootlast = now
            # fire bullet
            self.shoot()

        if now - self.movelast >= self.mvcooldown:
            self.movelast = now
            # move randomly
            self.handle_movement()

    # shoot
    '''
            print("left click")
            m_x, m_y = pygame.mouse.get_pos()
            p_x, p_y = self.get_pos()
            angle = math.atan2((m_y - p_y), (m_x - p_x))
            # make a bullet where the speed_x and speed_y = base_speed * math.cos(angle), base_speed * math.sin(angle)
            b = Bullet(p_x, p_y, 10, math.cos(angle), math.sin(angle))
            config.bullet_sprites.add(b)
            config.all_sprites.add(b)
    '''

    def shoot(self):
        p_x, p_y = self.get_pos()
        # make a bullet where the speed_x and speed_y = base_speed * math.cos(angle), base_speed * math.sin(angle)
        for i in range(0, 360, 30):
            rad = math.radians(i)
            c = 8
            # law of sines
            temp = c / math.sin(math.radians(90))
            a = temp * math.sin(rad)
            b = temp * math.sin(math.radians(90 - i))
            print(a, b)
            b = Bullet(p_x, p_y, 1, a, b)
            config.bullet_sprites.add(b)
            config.all_sprites.add(b)

    # handle_movement
    def handle_movement(self):
        temp = 1
        if random.randint(0, 2):
            temp = -1
        temp2 = 1
        if random.randint(0, 2):
            temp2 = -1

        self.rect.x += temp * self.speed
        self.rect.y += temp2 * self.speed

        # boundaries check
        if self.rect.right >= config.width:
            self.rect.right = config.width
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= config.height:
            self.rect.bottom = config.height

    def get_pos(self):
        return self.rect.centerx, self.rect.centery


class button():
    def __init__(self, color, x, y, width, height, text=''):
        # initialize properties of this particular button
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, screen, outlineColor=None):
        if outlineColor:
            pygame.draw.rect(screen, outlineColor, (self.x - 2, self.y - 2, self.width + 4, self.height + 4))

        # if you have pics instead of buttons -> load an image instead of drawing a rect
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

        if self.text != '':
            font = pygame.font.Font(font_name, 18)
            text_surface = font.render(self.text, True, config.colors["white"])
            screen.blit(text_surface, (self.x + (self.width / 2 - text_surface.get_width() / 2),
                                       self.y + (self.height / 2 - text_surface.get_height() / 2)))

    # check if a mouse click is inside the rect that is the button
    def inBoundaries(self, pos):
        if self.x < pos[0] < self.x + self.width and self.y < pos[1] < self.y + self.height:
            return True
        return False


class text_box(button):
    def __init__(self, color, x, y, width, height, text=''):
        if isinstance(text, str):
            text = [text]
        self.index = 0
        self.text_list = text
        super(text_box, self).__init__(color, x, y, width, height, self.text_list[self.index])

    def next(self):
        self.index += 1
        if self.index >= len(self.text_list):
            return True
        self.text = self.text_list[self.index]
        return False


def set_text(dialogue):
    # dialogue = [str(i) for i in range(10)]
    textbox = text_box(config.colors["black"], config.width // 2 - 100, config.height // 4, 100, 50, dialogue)
    start = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                if pygame.mouse.get_pressed() or pygame.key.get_pressed():
                    start = textbox.next()

        if start:
            break

        textbox.draw(config.screen, (255, 255, 255))
        pygame.display.update()


class item(pygame.sprite.Sprite):
    def __init__(self):
        # call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # [load] image or generate image
        self.image = pygame.Surface([30, 30])
        self.image.fill(config.colors["blue"])

        # initialize rect/hitbox
        self.rect = self.image.get_rect()

        # random spawn
        self.rect.x = random.randint(0, config.width)
        self.rect.y = random.randint(0, config.height)

    def update(self, player=None):
        # if player presses a specific key check if sprite collides with object
        if player:
            if pygame.key.get_pressed()[pygame.K_e]:
                if pygame.sprite.spritecollide(player, config.item_sprites,
                                               collided=pygame.sprite.collide_rect_ratio(2), dokill=True):
                    set_text("power up get!")
                    player.bullet_speed += 5
