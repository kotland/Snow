import sys
import pygame
from Classes.Button import Button
from settings import *

display = pygame.display.set_mode((500, 500))
screen = pygame.display.get_surface()  # определяем поверхность для рисования


class SelectBackground:
    def __init__(self):
        pygame.init()
        self.background = BACKGROUNG_IMG
        self.screen = pygame.display.set_mode((500, 500))
        self.btn_background1 = Button(pos=(150, 150), image_names=('button_on.png', 'button_hover.png',
                                                                   'button_click.png'),
                                      path=BUTTON_IMAGE_PATH,
                                      function=self.on_btn_background1, text='Background N1 ', w=200)
        self.btn_background2 = Button(pos=(150, 205),
                                      image_names=('button_on.png', 'button_hover.png', 'button_click.png'),
                                      path=BUTTON_IMAGE_PATH,
                                      function=self.on_btn_background2, text=' Background N2 ', w=200)
        self.btn_back_to_menu = Button(pos=(150, 260), image_names=('button_on.png', 'button_hover.png',
                                                                    'button_click.png'),
                                       path=BUTTON_IMAGE_PATH,
                                       function=self.on_btn_back_to_menu, text='Back to menu', w=200)
        self.work = True
        self.num_snows_scroll = None
        self.background_image = pygame.transform.scale(load_image(self.background, 0, IMAGE_PATH), PLATFORM)

    def on_btn_back_to_menu(self):
        from Classes.Menu import Menu

        self.work = False
        win_snow = Menu(background=self.background)
        win_snow.run()
        print('menu')

    def on_btn_background2(self):
        self.background = '3.jpg'
        self.background_image = pygame.transform.scale(load_image(self.background, 0, IMAGE_PATH), PLATFORM)
        print('Background2')

    def on_btn_background1(self):
        self.background = '4.jpg'
        self.background_image = pygame.transform.scale(load_image(self.background, 0, IMAGE_PATH), PLATFORM)
        print('background1')

    def render(self):
        self.screen.blit(self.background_image, (0, 0))
        self.btn_background1.render(self.screen)
        self.btn_back_to_menu.render(self.screen)
        self.btn_background2.render(self.screen)

    def event(self, event):
        self.btn_background1.event(event)
        self.btn_back_to_menu.event(event)
        self.btn_background2.event(event)

    def run(self):
        while self.work:
            self.screen.fill((10, 100, 100))

            for event in pygame.event.get():
                self.event(event)
                if event.type == pygame.QUIT:
                    sys.exit()

                    # self.update(0)
            self.render()
            # print(self.scrollbar.get_num())

            pygame.display.flip()


win = SelectBackground()
win.run()