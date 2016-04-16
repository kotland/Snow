import sys
import pygame

NUM_SNOWS = 20
FPS = 40


class Snow:
    def __init__(self):
        pass


class Program:
    def __init__(self):
        pygame.init()
        pygame.display.set_mode((500, 500))

        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        self.snow_list = []
        self.create_snow()

    def create_snow(self):
        # Create snow
        while len(self.snow_list) < NUM_SNOWS:
            pass

    def run(self):
        while True:
            for e in pygame.event.get():
                snow.events(e)
                if e.type == pygame.QUIT:
                    sys.exit()

                if e.type in (pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN):
                    for snow in self.snow_list:
                        snow.events(e)
                        # print(snow.status)
            dt = self.clock.tick(FPS)
            for snow in self.snow_list:
                snow.update(dt)

            self.screen.fill((0, 0, 0))
            for snow in self.snow_list:
                snow.render(self.screen)
            # angle += 1
            pygame.display.flip()


win = Program()
win.run()
