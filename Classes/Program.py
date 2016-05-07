import random
import settings
from Classes.Snow import Snow
# from Classes.Snow import snow_list
from Classes.Settings import *
import sys
import pygame

NUM_SNOWS = 20
FPS = 60

clock = pygame.time.Clock()


class Program:
    def __init__(self, num_snows):
        pygame.init()
        pygame.display.set_mode((500, 500))

        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        self.snow_list = []
        self.num_snows = num_snows
        self.create_snow()
        self.screen = pygame.display.get_surface()

    def on_btn_menu(self):
        from Classes.Menu import Menu
        self.work = False
        win_snow = Menu()
        win_snow.run()
        # print('menu')

    def create_snow(self):
        i = 0
        j = 0

        while len(self.snow_list) < self.num_snows:
            print(self.num_snows)
            i += 1
            # количество попыток пересоздания снежинки
            if j >= 300:
                break
            snow = Snow((random.randint(0, settings.PLATFORM[0]), (random.randint(0, settings.PLATFORM[1]))))
            collide_list = snow.check_area_list(self.snow_list)

            if len(collide_list) > 1:  # сколько пересечений должно быть в списке
                j += 1
                continue
            self.snow_list.append(snow)


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
                    for snow in self.snow_list:
                        snow.events(e)
                        # print(snow.status)
            dt = clock.tick(settings.FPS)
            for snow in self.snow_list:
                snow.update(dt)

            self.screen.fill((10, 100, 100))
            for snow in self.snow_list:
                snow.render(self.screen)
            angle += 1
            pygame.display.flip()

