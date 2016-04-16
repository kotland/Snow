import os
import sys

import pygame


class Text:  # простой класс, для вывода текста
    def __init__(self, text, x=0, y=0):
        self.x = x
        self.y = y
        self.text = text
        self.font = pygame.font.Font(None, 24)


def load_image(name, alpha_channel, dir_name):  # функция загрузки картинки (взята из примера)
    fullname = os.path.join(dir_name, name)  # путь картинки
    try:
        image = pygame.image.load(fullname)  # загрузка картинки
    except pygame.error:
        print("Cannot load image:", fullname)
        return 0
    if alpha_channel:  # если есть альфа канал, конвертирование картинки с учетом альфа канала
        image = image.convert_alpha()
    else:
        image = image.convert()  # если альфа канала нету, конвертирование без учета альфа канала

    return image


# Демонстрация использования класса для создания кнопки
def hello_world():
    print('Hello world!')


if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((640, 480))
    render_list = []
    # Создаем кнопку
    button = Button(pos=(10, 10), image_names=('button_off.png', 'button_hover.png', 'button_click.png'),
                    function=hello_world, text='Start! ', w=200)

    while True:
        screen.fill((10, 100, 10))

        for event in pygame.event.get():
            # Пересылаем все события кнопке
            button.event(event)
            if event.type == pygame.QUIT:
                sys.exit()

        # Обновляем и отрисовываем кнопку на экране
        button.update(0)
        button.render(screen)

        pygame.display.flip()
