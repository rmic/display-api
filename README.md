# API for simple displays

This API allows you to control displays, such as writing messages and moving the cursor.

## Endpoints
### GET /displays
Returns a list of available displays.

#### Example response:

```json
[{  "id": 0,
    "max_x": 19,        
    "max_y": 1    
}]
```
### POST /display/int:display_id/set_cursor
Moves the cursor on the specified display to the given position.

#### Parameters

- display_id: ID of the display to control.
- x: X coordinate of the new cursor position (integer).
- y: Y coordinate of the new cursor position (integer).

#### Example request:

```POST /display/0/set_cursor?x=5&y=0```

### POST /display/int:display_id/write
Writes a message on the specified display at the given position.

#### Parameters

- display_id: ID of the display to control.
- x: X coordinate of the position where the message will start (integer).
- y: Y coordinate of the position where the message will start (integer).
- message: Message to write (string).

#### Example request:

```
POST /display/0/write?x=0&y=0
Hello, world!
```

### POST /display/int:display_id/clear
Clears the specified display.

#### Parameters

- display_id: ID of the display to clear.

#### Example request:

```POST /display/0/clear```

## Functions 

### get_display(display_id)
Returns the display object with the given ID.

#### Parameters

- display_id: ID of the display to retrieve.

### validate_position(position, display)
Validates that the given position is within the bounds of the given display.

#### Parameters

- position: Dictionary with x and y keys representing the position to validate.
- display: Display object.

## Global Variables
- DISPLAYS : List of available display objects.