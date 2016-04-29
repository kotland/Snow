import sys
import pygame
from Classes.Button import Button
from Classes.Program import Program


display = pygame.display.set_mode((500, 500))

screen = pygame.display.get_surface()


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

