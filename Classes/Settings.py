import sys
import pygame
from Classes.Button import Button
from Classes.ScrollBar import ScrollBar


display = pygame.display.set_mode((500, 500))


class Settings:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        self.btn_start = Button(pos=(200, 150), image_names=('button_on.png', 'button_hover.png', 'button_click.png'),
                                path='../Buttons', function=self.on_btn_start, text='1 ', w=200)
        self.btn_settings = Button(pos=(200, 205),
                                   image_names=('button_on.png', 'button_hover.png', 'button_click.png'),
                                   path='../Buttons', function=self.on_btn_settings, text='Wind ', w=200)
        self.btn_exit = Button(pos=(200, 260), image_names=('button_on.png', 'button_hover.png', 'button_click.png'),
                               path='../Buttons', function=self.on_btn_exit, text='2 ', w=200)
        self.scrollbar = ScrollBar(200, 75, 100, text='Number snow')
        self.work = True

    def on_btn_exit(self):
        sys.exit()

    def on_btn_start(self):
        print('start')

    def on_btn_settings(self):
        print('settings')

    def render(self):
        self.btn_start.render(self.screen)
        self.btn_settings.render(self.screen)
        self.btn_exit.render(self.screen)
        self.scrollbar.render(self.screen)

    def event(self, event):
        self.btn_start.event(event)
        self.btn_settings.event(event)
        self.btn_exit.event(event)
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

            pygame.display.flip()


Settings_program = Settings()
Settings_program.run()