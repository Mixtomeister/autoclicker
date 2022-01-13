from pynput.mouse import Listener, Button, Controller

import threading
import time


delay = 0.00001
button = Button.left

class AutoClicker(threading.Thread):
    def __init__(self, delay, button):
        super(AutoClicker, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.keep_alive = True
        self.lock_position = None

    def start_clicker(self, lock_position=None):
        self.running = True
        self.lock_position = lock_position
        print('Autoclicker running!')

    def pause_clicker(self):
        self.running = False
        self.lock_position = None
        print('Autoclicker paused')

    def stop_clicker(self):
        self.pause_clicker()
        self.keep_alive = False

    def run(self):
        mouse = Controller()
        while self.keep_alive:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)

click_thread = AutoClicker(delay, button)
click_thread.start()

def on_click(x, y, button, pressed):
    if button == Button.x2:
        click_thread.start_clicker() if pressed else click_thread.pause_clicker()
    if button == Button.x1 and pressed:
        if not click_thread.running:
            click_thread.start_clicker(lock_position=(x, y))
        else:
            click_thread.pause_clicker()

def on_move(x, y):
    if click_thread.lock_position:
        if (x < click_thread.lock_position[0] - 100 or x > click_thread.lock_position[0] + 100) \
            or (y < click_thread.lock_position[1] - 100 or y > click_thread.lock_position[1] + 100):
            click_thread.pause_clicker()

with Listener(on_click=on_click, on_move=on_move) as listener:
    listener.join()