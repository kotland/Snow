class Menu:
    def __init__(self):
        # pygame.init()
        self.btn_start = Button()
        self.btn_settings = Button()

    def render(self):
        self.btn_start.render(self.screen)
        self.btn_settings.render(self.screen)

    def events(self, event):
        self.btn_start.events(event)
        self.btn_settings.events(event)

    def run(self):
        while True:
            pass
