import time
import pyautogui
import keyboard

class AutoClicker:
    def __init__(self):
        self.interval = 0.1  # Standard-Klickintervall in Sekunden
        self.duration = 0  # 0 für unbegrenzt
        self.is_clicking = False
        self.toggle_key = 't'

    def start_clicking(self):
        print(f"AutoClicker gestartet. Drücke '{self.toggle_key}' um ihn zu starten/pausieren oder 'Ctrl + C', um ihn zu stoppen.")
        end_time = time.time() + self.duration if self.duration else float('inf')

        while time.time() < end_time:
            if self.is_clicking:
                pyautogui.click()
            time.sleep(self.interval)

    def toggle_clicking(self):
        self.is_clicking = not self.is_clicking

def main():
    auto_clicker = AutoClicker()

    try:
        keyboard.add_hotkey(auto_clicker.toggle_key, auto_clicker.toggle_clicking)
        auto_clicker.start_clicking()
    except KeyboardInterrupt:
        print("\nAutoClicker durch Benutzer gestoppt.")
    finally:
        keyboard.remove_hotkey(auto_clicker.toggle_key)

if __name__ == "__main__":
    main()
