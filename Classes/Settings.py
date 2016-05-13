import sys
import pygame
from Classes.Button import Button
from Classes.ScrollBar import ScrollBar
from settings import *

display = pygame.display.set_mode((500, 500))


class Settings:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        self.btn_start = Button(pos=(200, 150), image_names=('button_on.png', 'button_hover.png',
                                                             'button_click.png'),
                                path=BUTTON_IMAGE_PATH,
                                function=self.on_btn_start, text='settings ', w=200)
        self.btn_settings_wind = Button(pos=(200, 205),
                                        image_names=('button_on.png', 'button_hover.png', 'button_click.png'),
                                        path=BUTTON_IMAGE_PATH,
                                        function=self.on_btn_settings_wind, text=' Background ', w=200)
        self.btn_back_to_menu = Button(pos=(200, 260), image_names=('button_on.png', 'button_hover.png',
                                                                    'button_click.png'),
                                       path=BUTTON_IMAGE_PATH,
                                       function=self.on_btn_back_to_menu, text='Back to menu', w=200)
        self.scrollbar = ScrollBar(200, 75, min_num=0, max_num=500, text='Number snow')
        self.work = True
        self.num_snows_scroll = None

    def on_btn_back_to_menu(self):
        from Classes.Menu import Menu

        self.work = False
        num_snows_scroll = self.scrollbar.get_num()  # кол-во снежинок = значение снежинок на скроллинге
        print("from sc = ", num_snows_scroll)
        win_snow = Menu(num_snows_scroll)
        win_snow.run()

    def on_btn_settings_wind(self):
        print('Background')

    def on_btn_start(self):
        print('1')

    def render(self):
        self.btn_start.render(self.screen)
        self.btn_back_to_menu.render(self.screen)
        self.btn_settings_wind.render(self.screen)
        self.scrollbar.render(self.screen)

    def event(self, event):
        self.btn_start.event(event)
        self.btn_back_to_menu.event(event)
        self.btn_settings_wind.event(event)
        self.scrollbar.event(event)

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


            # Settings_program = Settings()
            # Settings_program.run()