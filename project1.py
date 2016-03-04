# отладить пересечение снежинок при разных  скоростях
import os
import sys
import random
import pygame

from Vector import Vector


FPS = 60
MOVE_DOWN = 4
NORMAL = 0
PLATFORM = (500, 500)
speed_snow = Vector((0, random.randint(3, 4)))


def load_image(name, alpha_cannel):
    fullname = os.path.join('examples', name)
    # print(fullname)

    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print("Cannot load image:", name)
        return 0
    if alpha_cannel:
        image = image.convert_alpha()
    else:
        image = image.convert()

    return image


class Snow:
    def __init__(self, pos):
        self.image = load_image('11037430.gif', 1)
        self.pos = Vector(pos)
        self.speed = Vector((0, 1))
        self.status = NORMAL
        self.transform()
        self.angle = 6
        w, h = 55, 55
        self.area = pygame.Rect(0, 0, w, h)


    def events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.status = MOVE_DOWN

    def draw_rect(self, screen):
        self.area.center = self.pos.as_point()
        pygame.draw.rect(screen, (0, 200, 0), self.area, 2)

    def update(self, dt):
        if self.pos.x > PLATFORM[0]:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = PLATFORM[0]
        if self.pos.y > PLATFORM[1]:
            print("recreate --> ", self.check_area_list(snow_list))
            self.pos.y = random.randint(-100, -50)
            self.pos.x = random.randint(0, PLATFORM[0])
            # проверка списка с пересечениями при пересоздании
            while len(self.check_area_list(snow_list)) > 5:
                self.pos.y = random.randint(-100, -50)
                self.pos.x = random.randint(0, PLATFORM[0])
            self.speed = speed_snow
        self.move()


    def check_area_list(self, obj_list):
        obj_list = [obj.area.move(obj.pos.as_point()) for obj in obj_list if
                    not obj is self]  # создается список и пересекаемыми объектами
        area = self.area.move(self.pos.as_point())
        return area.collidelistall(obj_list)

    # def check_area(self, obj_list):
    # obj_list = [obj.rect for obj in obj_list if not obj is self]  # создается список и пересекаемыми объектами и выводится
    # # print(self.area.collidelistall(obj_list))

    def move(self):
        if self.status == MOVE_DOWN:
            self.pos += self.speed

    def render(self, screen):
        self.rect = self.image.get_rect()  # создаем прямоугольник вокруг объекта
        self.rect.center = self.pos.as_point()  # центрируем в нем объект
        pygame.draw.rect(screen, (100, 0, 100), self.rect, 1)
        screen.blit(self.image, self.rect)

    def transform(self):
        self.image = pygame.transform.scale(self.image, (60, 50))


NUM_SNOWS = 100

pygame.init()
display = pygame.display.set_mode((500, 500))

screen = pygame.display.get_surface()
snow_list = []
# snow_coords = [(100, 100), (110, 100), (225, 250), (250, 250)] # координаты снежинок для проверки пересечений
i = 0
j = 0

while len(snow_list) < NUM_SNOWS:
    i += 1
    if j >= 300:
        break
    else:
        # snow = Snow(snow_coords[_])
        snow = Snow((random.randint(0, PLATFORM[0]), (random.randint(0, PLATFORM[1]))))
        collide_list = snow.check_area_list(snow_list)
        if len(collide_list) >= 1:  # сколько пересечений должно быть в списке
            j += 1
            continue
        else:
            print("snow", i, "with", collide_list)
            snow_list.append(snow)

            clock = pygame.time.Clock()

print('num snows', len(snow_list))

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()

        if e.type in (pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN):
            for snow in snow_list:
                snow.events(e)

    dt = clock.tick(FPS)
    for snow in snow_list:
        snow.update(dt)

    screen.fill((0, 0, 0))
    for snow in snow_list:
        snow.render(screen)

    pygame.display.flip()


