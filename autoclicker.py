from pynput.mouse import Button, Listener, Controller
import threading
import time
import random

mouse = Controller()
btn_click = Button.left
btn_listen = Button.button8
is_down = False
# pause = 0.01 # Minimum mouse click delay (unused)
cps_range = [i for i in range(10, 14)] # From 10 to 14 CPS

def on_click(x, y, button, pressed):
	global is_down
	if button == btn_listen:
		print(f"State: {pressed}")
		is_down = pressed

listener = Listener(on_click=on_click)
listener.start()

while True:
	if is_down:
		mouse.click(btn_click)
		time.sleep(1 / random.choice(cps_range))
