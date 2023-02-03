# Interface to manage various kinds of hardware display
import enum

import displays.manager

class CounterType(enum.Enum):
    NUMERIC = 0,
    PROGRESS_BAR = 1

class DisplayInterface:
    def __init__(self, hardware_display):
        # Keep Hardware Display
        self.__display = hardware_display
        self.__nb_displays = hardware_display.get_available_displays()
        self.__counters = {}

    def __validate_display_id(self, display_id):
        if display_id > self.__display.get_available_displays() - 1 or display_id < 0:
            raise ValueError("Invalid display id")
    def get_available_displays(self):
        return str(self.__nb_displays)

    def set_cursor_position(self, display_id, position):
        self.__validate_display_id(display_id)
        self.__display.set_cursor_position(display_id, int(position['x']), int(position['y']))

    def print_message(self, display_id, message):
        self.__validate_display_id(display_id)
        self.__display.print_message(display_id, message)

    def clear(self, display_id):
        self.__validate_display_id(display_id)
        self.__display.clear(display_id)

    def init_counter(self, display_id, label, label_position=(0,0), value_position=(0,1), counter_type:CounterType=CounterType.NUMERIC, initial_value=0, default_step=1, min_value=None, max_value=None):
        self.__validate_display_id(display_id)

        if min_value is not None and initial_value < min_value:
            raise ValueError(f'Initial counter value {initial_value} below minimum {min_value}')

        if max_value is not None and initial_value > max_value:
            raise ValueError(f'Initial counter value {initial_value} above maximum {max_value}')

        self.__counters[display_id] = dict(initial_value=initial_value,
                                           current_value=initial_value,
                                           default_step=default_step,
                                           min_value=min_value,
                                           max_value=max_value,
                                           label=label,
                                           label_position=label_position,
                                           value_position=value_position,
                                           counter_type=counter_type
                                        )

        #TODO: Display counter

    def step_counter(self, display_id, step=None):
        self.__validate_display_id()
        if display_id in self.__counters:
            current_value = self.__counters.get(display_id).get('current_value')
            step_value = step if step is not None else self.__counters.get(display_id).get('default_step')
            self.set_counter_value(display_id, (current_value+step_value))
        else:
            raise ValueError('No counter found for this display')


    def set_counter_value(self, display_id, value):
        self.__validate_display_id()
        if display_id in self.__counters:
            counter = self.__counters.get(display_id)
            if (value is None) or (counter['min_value'] is not None and value <= counter['min_value']) or (counter['max_value'] is not None and value >= counter['min_value']):
                raise ValueError(f"Counter value {value} is out of bounds [{counter['min_value']}, {counter['max_value']}]")

            self.__counters[display_id]['current_value'] = value
            #TODO: Update display
        else:
            raise ValueError('No counter found for this display')
    def reset_counter(self, display_id):
        self.__validate_display_id()
        if display_id in self.__counters:
            counter = self.__counters.get(display_id)
            self.set_counter_value(display_id, counter['initial_value'])

    def remove_counter(self, display_id):
        self.__validate_display_id()
        if display_id in self.__counters:
            del self.__counters[display_id]
            #TODO: Update display