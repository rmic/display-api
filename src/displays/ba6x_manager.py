# Abstraction of BA6X displays

from vfdwcn import vfdwcn, WincorNixdorfDisplayFactory

class BA6XDisplayManager:
    def __init__(self):
        factory = WincorNixdorfDisplayFactory()
        self.__vfds = factory.get_vfd_wcn(vfdwcn.BA63)
        self.__nb_displays = len(self.__vfds)
        self.__max_x = 19
        self.__max_y = 1

    def get_available_displays(self):
        return self.__nb_displays

    def set_cursor_position(self, display_id, x, y):
        if x > self.__max_x or x < 0 or y > self.__max_y or y < 0:
            raise ValueError("Invalid cursor position")
        self.__vfds[display_id].poscur(x, y)

    def print_message(self, display_id, message):
        self.__vfds[display_id].write_msg(message)

    def clear(self, display_id):
        self.__vfds[display_id].clearscreen()
