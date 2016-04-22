# menu

import random
import settings
from Classes.Snow import Snow
from Classes.Snow import snow_list
import sys
import pygame
from Classes.Button import Button

NUM_SNOWS = 20
FPS = 60
pygame.init()
display = pygame.display.set_mode((500, 500))

screen = pygame.display.get_surface()

i = 0
j = 0
clock = pygame.time.Clock()


class Menu:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        self.btn_start = Button(pos=(200, 150), image_names=('button_on.png', 'button_hover.png', 'button_click.png'),
                                path='Buttons', function=self.on_btn_start, text='Start! ', w=200)
        self.btn_settings = Button(pos=(200, 205),
                                   image_names=('button_on.png', 'button_hover.png', 'button_click.png'),
                                   path='Buttons', function=self.on_btn_settings, text='Settings ', w=200)
        self.btn_exit = Button(pos=(200, 260), image_names=('button_on.png', 'button_hover.png', 'button_click.png'),
                               path='Buttons', function=self.on_btn_exit, text='Exit ', w=200)
        self.work = True

    def on_btn_exit(self):
        sys.exit()

    def on_btn_start(self):
        self.work = False
        win_snow = Program()
        win_snow.run()
        # print('start')


    def on_btn_settings(self):
        print('settings')

    def render(self):
        self.btn_start.render(self.screen)
        self.btn_settings.render(self.screen)
        self.btn_exit.render(self.screen)

    def event(self, event):
        self.btn_start.event(event)
        self.btn_settings.event(event)
        self.btn_exit.event(event)

    def run(self):
        while self.work:
            self.screen.fill((10, 100, 100))

            for event in pygame.event.get():
                self.event(event)
                if event.type == pygame.QUIT:
                    sys.exit()

                    # self.update(0)
            self.render()

            pygame.display.flip()


class Program:
    def __init__(self):
        pygame.init()
        pygame.display.set_mode((500, 500))

        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        self.snow_list = []
        self.create_snow()

    def on_btn_menu(self):
        self.work = False
        win_snow = Menu()
        win_snow.run()
        # print('menu')

    def create_snow(self):
        # Create snow
        i = 0
        j = 0
        while len(snow_list) < settings.NUM_SNOWS:
            i += 1
            # количество попыток пересоздания снежинки
            if j >= 300:
                break
            snow = Snow((random.randint(0, settings.PLATFORM[0]), (random.randint(0, settings.PLATFORM[1]))))
            collide_list = snow.check_area_list(snow_list)

            if len(collide_list) > 1:  # сколько пересечений должно быть в списке
                j += 1
                continue
            snow_list.append(snow)


        # print('num snows', len(snow_list))

    def run(self):
        angle = 0
        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.MOUSEBUTTONDOWN:
                    self.on_btn_menu()

                if e.type in (pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN):
                    for snow in snow_list:
                        snow.events(e)
                        # print(snow.status)
            dt = clock.tick(settings.FPS)
            for snow in snow_list:
                snow.update(dt)

            screen.fill((10, 100, 100))
            for snow in snow_list:
                snow.render(screen)
            angle += 1
            pygame.display.flip()



win = Menu()
win.run()
