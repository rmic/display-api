# Abstraction of hardware displays

class DisplayManager:
    def __init__(self):
        # Keep Hardware Display
        self.__nb_displays = 1
        self.__max_x = 19
        self.__max_y = 1

    def get_available_displays(self):
        return self.__nb_displays

    def set_cursor_position(self, display_id, x, y):
        if x > self.__max_x or x < 0 or y > self.__max_y or y < 0 :
            raise ValueError("Invalid cursor position")
        print("Cursor at x=" + str(x) + ", y=" + str(y))

    def print_message(self, display_id, message):
        print(message)

    def clear(self, display_id):
        print("-- Clear screen --")
