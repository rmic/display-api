from flask import Flask, request
import display_interface
import displays.manager

app = Flask(__name__)


@app.route('/displays', methods=['GET'])
def get_available_displays():
    return di.get_available_displays(), 202

@app.route('/display/<int:display_id>/set_cursor', methods=['POST'])
def set_cursor(display_id):
    try:
        position = request.args.to_dict()
        print(position)
        # send the message to the display
        di.set_cursor_position(display_id, position)
        return 'wilco', 202
    except ValueError as e:
        return str(e), 400


@app.route('/display/<int:display_id>/write', methods=['POST'])
def write_message(display_id):
    try:
        message = str(request.data)

        di.print_message(display_id, message)
        return 'wilco', 202
    except ValueError as e:
        return str(e), 400


@app.route('/display/<int:display_id>/clear', methods=['POST'])
def clear_display(display_id):
    try:
        di.clear(display_id)
        return 'wilco', 202
    except ValueError as e:
        return str(e), 400


@app.route('/brew', methods=['POST', 'BREW'])
def brew():
    return "I'm a teapot", 418


if __name__ == '__main__':
    print("Test with a dummy display")
    dm = displays.manager.DisplayManager()
    di = display_interface.DisplayInterface(dm)

    app.run()
