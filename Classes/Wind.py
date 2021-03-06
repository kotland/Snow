from Vector import Vector


class Wind:
    def __init__(self, x, y, blow_time, stop_time):
        self.dir = Vector((x, y))
        self.temp = self.dir
        self.time = 0
        self.timings = [blow_time, stop_time]
        self.blow = True


class ConstantWind(Wind):
    def update(self, dt):
        # время изменения ветра
        self.time += dt
        self.time += dt
        if self.time >= 1000:
            self.time = 0
            self.dir *= -1


class StrongWind(Wind):
    def update(self):
        # ветер сильный
        if self.time >= self.timings[self.blow]:
            self.time = 0
            self.blow = not self.blow
            if self.blow:
                self.dir = self.temp
            else:
                self.dir = Vector((0, 0))
