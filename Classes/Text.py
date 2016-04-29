import pygame


class Text:  # простой класс, для вывода текста
    def __init__(self, text, x=0, y=0):
        self.x = x
        self.y = y
        self.text = text
        self.font = pygame.font.Font(None, 24)

    def render(self, screen):
        surf = self.font.render(str(self.text), True, (90, 0, 40))
        screen.blit(surf, (self.x, self.y))


