import json

from flask import Flask, request
import display_interface
import displays.ba6x_manager

display_api = Flask(__name__)
dm = displays.ba6x_manager.BA6XDisplayManager()
di = display_interface.DisplayInterface(dm)

@display_api.route('/displays', methods=['GET'])
def get_available_displays():
    return di.get_available_displays(), 202

@display_api.route('/display/<int:display_id>/set_cursor', methods=['POST'])
def set_cursor(display_id):
    try:
        position = request.args.to_dict()
        # send coordinates to the display
        di.set_cursor_position(display_id, position)
        return 'wilco', 202
    except ValueError as e:
        return str(e), 400

@display_api.route('/display/<int:display_id>/write', methods=['POST'])
def write_message(display_id):
    try:
        # request data needs to be converted to avoid b'" display
        # TODO: auto decode
        message = request.data.decode('UTF-8')
        di.print_message(display_id, message)
        return 'wilco', 202
    except ValueError as e:
        return str(e), 400

@display_api.route('/display/<int:display_id>/clear', methods=['POST'])
def clear_display(display_id):
    try:
        di.clear(display_id)
        return 'wilco', 202
    except ValueError as e:
        return str(e), 400


@display_api.route('/display/<int:display_id>/counter', methods=['POST'])
def init_counter(display_id):
    try:
        data = json.parse(request.data.decode('UTF-8'))
        #TODO : clean data dict before calling
        di.init_counter(display_id, **data)
    except ValueError as e:
        return str(e), 400
    except Exception as e:
        return str(e), 500

@display_api.route('/display/<int:display_id>/counter/step', methods=['POST'])
def step_counter(display_id):
    try:
        args = request.args.to_dict() if request.args else dict()
        di.step_counter(display_id, args.get('v', None))
    except ValueError as e:
        return str(e), 400
    except Exception as e:
        return str(e), 500

@display_api.route('/display/<int:display_id>/counter', methods=['PUT'])
def set_counter_value(display_id):
    try:
        args = request.args.to_dict() if request.args else dict()
        di.set_counter_value(display_id, args.get('v', None))
    except ValueError as e:
        return str(e), 400
    except Exception as e:
        return str(e), 500

@display_api.route('/display/<int:display_id>/counter', methods=['DELETE'])
def step_counter(display_id):
    try:
        di.remove_counter(display_id)
    except ValueError as e:
        return str(e), 400
    except Exception as e:
        return str(e), 500


@display_api.route('/brew', methods=['POST', 'BREW'])
def brew():
    return "I'm a teapot", 418


if __name__ == '__main__':
    display_api.run()
