import random
import pygame
from settings import *
import helpers
from Vector import Vector
from Classes.Wind import StrongWind, ConstantWind


class Snow:
    def __init__(self, pos):
        self.image = helpers.load_image('11037430.gif', 1, SNOW_IMAGE_PATH)
        self.pos = Vector(pos)
        self.speed = Vector((0, 5))
        self.transform()
        # self.angle = 6
        self.snow_list = []
        self.status = MOVE_DOWN
        wind1 = StrongWind(0.01, 0, 1, 0)
        wind2 = ConstantWind(-0.05, 0, random.randint(2000, 3000), 7000)
        self.winds = [wind1, wind2]
        w, h = 55, 55
        self.area = pygame.Rect(0, 0, w, h)

    def draw_rect(self, screen):
        self.area.center = self.pos.as_point()
        pygame.draw.rect(screen, (0, 200, 0), self.area, 2)

    def update(self, dt):

        if self.pos.x > PLATFORM[0]:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = PLATFORM[0]
        elif self.pos.y > PLATFORM[1]:
            # print("recreate --> ", self.check_area_list(self.snow_list))
            self.pos.y = random.randint(-100, -50)
            self.pos.x = random.randint(0, PLATFORM[0])
            self.speed = Vector((0, random.randint(4, 5)))  # меняем скорость при пересоздании
            # проверка списка с пересечениями при пересоздании
            while len(self.check_area_list(self.snow_list)) >= 2:
                self.pos.y = random.randint(-100, -50)
                self.pos.x = random.randint(0, PLATFORM[0])
                self.speed = Vector((0, random.randint(4, 6)))  # меняем скорость при пересоздании
        self.move()
        self.speed += self.winds[0].dir + self.winds[1].dir

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
        ''

        # ресуем  вектор скорости
        # ВЕКТОР
        # dv = Vector((self.image.get_rect().w / 2, self.image.get_rect().h / 2))
        # p1 = self.pos.as_point()
        # p2 = (self.pos + self.speed*10).as_point()
        # pygame.draw.line(screen, (100, 200, 200), p1, p2)
        ''

        self.rect = self.image.get_rect()  # создаем прямоугольник вокруг объекта
        self.rect.center = self.pos.as_point()  # центрируем в нем объект
        # ПРЯМОУГОЛЬНИК
        # pygame.draw.rect(screen, (100, 0, 100), self.rect, 1)
        screen.blit(self.image, self.rect)

    def transform(self):
        self.image = pygame.transform.scale(self.image, (60, 50))
