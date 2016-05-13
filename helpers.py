import os
import pygame


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
        # pass
        image = image.convert()  # если альфа канала нет, конвертирование без учета альфа канала

    return image
