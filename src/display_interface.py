# Interface to manage various kinds of hardware display
import displays.manager


class DisplayInterface:
    def __init__(self, hardware_display):
        # Keep Hardware Display
        self.__display = hardware_display
        self.__nb_displays = hardware_display.get_available_displays()

    def get_available_displays(self):
        return self.__nb_displays

    def set_cursor_position(self, display_id, position):
        if display_id > self.__display.get_available_displays() - 1 or display_id < 0:
            raise ValueError("Invalid display id")
        self.__display.set_cursor_position(display_id, int(position['x']), int(position['y']))

    def print_message(self, display_id, message):
        if display_id > self.__display.get_available_displays() - 1 or display_id < 0:
            raise ValueError("Invalid display id")
        self.__display.print_message(display_id, message)

    def clear(self, display_id):
        if display_id > self.__display.get_available_displays() - 1 or display_id < 0:
            raise ValueError("Invalid display id")
        self.__display.clear(display_id)
