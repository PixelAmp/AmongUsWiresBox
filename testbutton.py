:import RPi.GPIO as GPIO
import time


pin = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setwarnings(False)


while True:
	input_state = GPIO.input(pin)
	if input_state == False:
        	print('Button Pressed')
        	time.sleep(0.2)
