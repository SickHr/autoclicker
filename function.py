# imports
import threading
from pynput.keyboard import KeyCode, Controller
from pynput.mouse import Listener, KeyCode


# auto clicker funktion

class Function:
    def __int__(self, time):
        self.toggle = KeyCode(char='t')

        self.time = time
        self.is_clicking = False

    def click(self):
        while self.is_clicking:
            self.pyautogui.click()
            time.sleep(self.time)

    def start(self):
        pass
