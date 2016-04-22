import sys
import random
import pygame
import settings
from Classes.Snow import Snow
from Classes.Snow import snow_list
pygame.init()
display = pygame.display.set_mode((500, 500))

screen = pygame.display.get_surface()
clock = pygame.time.Clock()

i = 0
j = 0

# Create snow
while len(snow_list) < settings.NUM_SNOWS:
    i += 1
    # количество попыток пересоздания снежинки
    if j >= 300:
        break
    snow = Snow((random.randint(0, settings.PLATFORM[0]), (random.randint(0, settings.PLATFORM[1]))))
    collide_list = snow.check_area_list(snow_list)

    if len(collide_list) > 1:  # сколько пересечений должно быть в списке
        j += 1
        continue
    snow_list.append(snow)

    clock = pygame.time.Clock()

print('num snows', len(snow_list))
angle = 0
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()

        if e.type in (pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN):
            for snow in snow_list:
                snow.events(e)
                # print(snow.status)
    dt = clock.tick(settings.FPS)
    for snow in snow_list:
        snow.update(dt)

    screen.fill((10, 100, 100))
    for snow in snow_list:
        snow.render(screen)
    angle += 1
    pygame.display.flip()
