import pygame
from Classes.ScrollBar import ScrollBar

class Place_editor:
    """
    Класс согласует работу (раздает события, отрисовывает) объектов редактора
    (самого поля, ползунков, палитр и т.д.)
    """

    def __init__(self, wh):
        self.objs_list = []  # список перемещаемых объектов
        self.static_objects_list = []  # список не перемещаемых объектов
        self.image = pygame.Surface(wh, pygame.SRCALPHA)  # поверхность редактора, на которую рендерятся все объекты
        self.scroll = ScrollBar(10, 30, 50, 1, text='number snow:')  # ползунок, устанавливающий кол-во снежинок

        self.objs_list_for_events = []

    def event(self, e):
        """
        метод передает кому надо, какие надо события
        """

        if e.type == pygame.MOUSEMOTION:  # событие движения мыши отдельно передается всем объектом, кроме тому, который
            # в фокусе, тому и так предастся. Только для красоты.
            for obj in self.objs_list_for_events[1:]:
                obj.event(e)

        if e.type == pygame.MOUSEBUTTONDOWN:  # при нажатии клавиши мыши, определяется объект в фокусе (на который ткнули)
            # и перемещается в начало списка объектов для передачи событий
            for i in range(0, len(self.objs_list_for_events)):
                if self.objs_list_for_events[i].check_mouse_coords(e.pos):
                    self.objs_list_for_events[i].CursorOnImage = True
                    self.objs_list_for_events.insert(0, self.objs_list_for_events[i])
                    self.objs_list_for_events.pop(i + 1)
                    break
            for i in range(0, len(self.objs_list)):
                if self.objs_list[i].check_mouse_coords(e.pos):
                    self.objs_list[i].CursorOnImage = True
                    self.objs_list.insert(0, self.objs_list[i])
                    self.objs_list.pop(i + 1)
                    break

        if e.type == USEREVENT + 1:  # событие движения ползунка, передается полю, чтобы то изменило свой размер,
            #даже если поле не находится в фокусе
            self.field.event(e)

        self.objs_list_for_events[0].event(e)  # ВСЕ события передаются объекту, который в фокусе

