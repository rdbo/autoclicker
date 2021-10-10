from pynput.mouse import Button, Listener, Controller
import time
import random
import argparse

mouse = Controller()
buttons = {
	"left" : Button.left,
	"right" : Button.right,
	"middle" : Button.middle,
	"x1" : Button.button8,
	"x2" : Button.button9
}
btn_listen = None
btn_click = None
cps_delays = []
is_pressed = False

def on_click(x, y, button, pressed):
	global is_pressed
	if button == btn_listen:
		print(f"{button} : {pressed}")
		is_pressed = pressed


if __name__ == "__main__":
	btn_options = [btn for btn in buttons]
	parser = argparse.ArgumentParser()
	parser.add_argument("-l", "--listen", action="store", dest="listen", default=btn_options[-1], choices=btn_options, required=False)
	parser.add_argument("-c", "--click", action="store", dest="click", default=btn_options[0], choices=btn_options, required=False)
	parser.add_argument("-m", "--min", action="store", dest="min", default=8, type=int, required=False)
	parser.add_argument("-x", "--max", action="store", dest="max", default=16, type=int, required=False)
	args = parser.parse_args()
	if args.min > args.max:
		parser.print_help()
		exit(0)
	btn_listen = buttons[args.listen]
	btn_click = buttons[args.click]
	cps_delays = [(1 / i) for i in range(args.min, args.max + 1)]
	listener = Listener(on_click=on_click)
	listener.start()

	while True:
		if is_pressed:
			mouse.click(btn_click)
			time.sleep(random.choice(cps_delays))
