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
        self.btn_back_to_menu = None
        self.work = True
        self.background_image = pygame.transform.scale(load_image(self.background, 0, IMAGE_PATH), PLATFORM)
        self.backgrounds = ['3.jpg', '4.jpg', '6.jpg', '5.jpg']
        self.buttons = []
        self.button_constructor()
        self.button_clicked = False

    def on_btn_back_to_menu(self):
        from Classes.Settings import Settings

        self.work = False
        win_snow = Settings(background=self.background)
        win_snow.run()

    def on_btn(self):
        self.button_clicked = True

    def render(self):
        self.screen.blit(self.background_image, (0, 0))
        self.btn_back_to_menu.render(self.screen)
        for button in self.buttons:
            button.render(self.screen)

    def event(self, event):
        self.btn_back_to_menu.event(event)
        for num, button in enumerate(self.buttons):
            # кидаем event каждой кнопке. Если эта кнопка была нажата, переключает флаг
            button.event(event)
            if self.button_clicked:
                self.change_image(num)
                self.button_clicked = False

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

    def button_constructor(self):
        # Метод создаёт кнопки, в зависимости от кол-ва картинок и автоматичекси размещает на расстоянии 55px
        y = 100  # Расстояние первой кнопки от верхнего края
        for i, image in enumerate(self.backgrounds):  # enumerate() возвращает индекс элемента и его значение
            self.buttons.append(Button(pos=(150, y), image_names=('button_on.png', 'button_hover.png',
                                                                  'button_click.png'), path=BUTTON_IMAGE_PATH,
                                       function=self.on_btn, text=' Background N%s ' % (i+1), w=200))
            y += 55
        self.btn_back_to_menu = Button(pos=(150, y), image_names=('button_on.png', 'button_hover.png',
                                                                  'button_click.png'), path=BUTTON_IMAGE_PATH,
                                       function=self.on_btn_back_to_menu, text='Back to menu', w=200)

    def change_image(self, image_num):
        self.background = self.backgrounds[image_num]
        # Изменяет задний фон этого окна
        self.background_image = pygame.transform.scale(load_image(self.background, 0, IMAGE_PATH), PLATFORM)


win = SelectBackground()
win.run()
