import sys
from pygame import Rect
from Classes.Button import Button
from Classes.ScrollBar import ScrollBar
from settings import *

display = pygame.display.set_mode((500, 500))


class Settings:
    def __init__(self, background=BACKGROUNG_IMG, pos=(0, 0), size=(20, 20)):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))
        self.btn_settings_wind = Button(pos=(150, 205),
                                        image_names=('button_on.png', 'button_hover.png', 'button_click.png'),
                                        path=BUTTON_IMAGE_PATH,
                                        function=self.on_btn_settings_wind, text=' Background ', w=200)
        self.btn_back_to_menu = Button(pos=(150, 260), image_names=('button_on.png', 'button_hover.png',
                                                                    'button_click.png'),
                                       path=BUTTON_IMAGE_PATH,
                                       function=self.on_btn_back_to_menu, text='Back to menu', w=200)
        self.scrollbar = ScrollBar(150, 150, min_num=50, max_num=5000, text='Number snow')
        self.work = True
        self.num_snows_scroll = None
        self.background = background
        self.background_image = pygame.transform.scale(load_image(self.background, 0, IMAGE_PATH), PLATFORM)
        self.rect = pygame.Rect(pos, size)

    def on_btn_back_to_menu(self):
        from Classes.Menu import Menu

        self.work = False
        num_snows_scroll = self.scrollbar.get_num()  # кол-во снежинок = значение снежинок на скроллинге
        print("from sc = ", num_snows_scroll)
        win_snow = Menu(num_snows_scroll)
        win_snow.run()

    def on_btn_settings_wind(self):
        from Classes.Background import SelectBackground

        win_snow = SelectBackground()
        win_snow.run()
        print('Background')

    def draw(self):
        pygame.draw.rect(self.screen, (10, 100, 100), Rect((145, 127), (212, 70)))

    def render(self):
        self.screen.blit(self.screen, self.rect)
        self.btn_back_to_menu.render(self.screen)
        self.btn_settings_wind.render(self.screen)
        self.scrollbar.render(self.screen)

    def event(self, event):
        self.btn_back_to_menu.event(event)
        self.btn_settings_wind.event(event)
        self.scrollbar.event(event)

    def run(self):
        while self.work:
            self.screen.blit(self.background_image, (0, 0))
            self.draw()

            for event in pygame.event.get():
                self.event(event)
                if event.type == pygame.QUIT:
                    sys.exit()

                    # self.update(0)
            self.render()

            pygame.display.flip()

