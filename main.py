import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

TOGGLE_KEY = KeyCode(char='t')
mouse = Controller()

clicking = False

click_speed = 0.005

def clicker():
    while True:
        if clicking:
            mouse.click(Button.left)

        time.sleep(click_speed)


def toggling_event(key):
    if key == TOGGLE_KEY:
        global clicking
        clicking = not clicking
        print(clicking)


threading.Thread(target=clicker).start()
with Listener(on_press=toggling_event) as listener:
    listener.join()
