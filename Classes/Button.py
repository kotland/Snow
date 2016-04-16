import pygame
import helpers

from Classes import Text_Button


class Button:  # основная кнопка
    def __init__(self, image_names, path='../Images/Buttons', pos=(0, 0), function=None, parent=None,
                 text='Simple Button',
                 w=0, h=0):
        self.image_normal = helpers.load_image(image_names[0], alpha_channel=True,
                                               dir_name=path)  # изображение кнопки в базовом состоянии
        self.image_on_over = helpers.load_image(image_names[1], alpha_channel=True,
                                                dir_name=path)  # изображение кнопки в базовом состоянии
        self.image_on_click = helpers.load_image(image_names[2], alpha_channel=True,
                                                 dir_name=path)  # изображение кнопки в базовом состоянии
        self.images = [self.image_normal, self.image_on_over, self.image_on_click]  # список с кнопками
        if w != 0 and h != 0:  # изменение размера картинки, если заданы ширина и высота
            for i in range(0, 3):
                self.images[i] = pygame.transform.scale(self.images[i], (w, h))
        elif w != 0 and h == 0:  # если задан один размер, то второй изменяется пропорционально
            for i in range(0, 3):
                rect = self.images[i].get_rect()
                h = int(rect.h * (w / rect.w))
                self.images[i] = pygame.transform.scale(self.images[i], (w, h))
        elif w == 0 and h != 0:
            for i in range(0, 3):
                rect = self.images[i].get_rect()
                w = int(rect.w * (h / rect.h))
                self.images[i] = pygame.transform.scale(self.images[i], (w, h))

        self.current_image = self.images[0]  # текущая картинка

        self.rect = self.current_image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

        self.text = Text_Button.Text(text)  # текст кнопки
        self.text_surf = self.text.font.render(text, True, (0, 0, 0))  # поверхность текста
        self.rect_text = self.text_surf.get_rect()  # рект текста
        # смещение текста на центр картинки кнопки,
        self.rect_text.x = self.rect.x + self.rect.w / 2 - self.rect_text.w / 2
        # к координате кнопки прибавляется половина длины картинки и отнимается половина длины текста
        self.rect_text.y = self.rect.y + self.rect.h / 2 - self.rect_text.h / 2

        self.function = function  # функция кнопки
        self.parent = parent  # родитель кнопки, по умолчанию отсутствует

    def event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.check_mouse_coords(event.pos):
                if self.parent:
                    parametrs = self.parent.get_parametrs_for_function()  # получает от родителя
                    self.function(parametrs)  # вызывает с функцию с передачей аргументов
                elif self.function:
                    self.function()  # если родителя нет, то функция вызывается без передачи аргументов
                self.change_image('click')

        if event.type == pygame.MOUSEBUTTONUP:
            if self.check_mouse_coords(event.pos):
                self.change_image('over')

        if event.type == pygame.MOUSEMOTION:
            if self.check_mouse_coords(event.pos):  # если курсор на картинке, смена картинки
                self.change_image('over')  # метод смены картинки
            elif not self.check_mouse_coords(event.pos):
                self.change_image('normal')

    def change_image(self, status):  # смена картинки в зависимости от статуса
        if status == 'normal':
            self.current_image = self.images[0]
        elif status == 'over':
            self.current_image = self.images[1]
        elif status == 'click':
            self.current_image = self.images[2]

    def check_mouse_coords(self, xy):  # проверяет, находятся ли координаты мыши в ректе картинки
        if self.rect.collidepoint(xy):
            return True
        else:
            return False

    def update(self, dt):
        pass

    def render(self, screen):
        screen.blit(self.current_image, self.rect)  # на экран рисуется картинка кнопка
        screen.blit(self.text_surf, self.rect_text)
