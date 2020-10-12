import RPi.GPIO as GPIO
import time



def main():
	LEDpin = 21         # The pin connected to the LED
	BUTTONpin = 19      # The pin connected to the button
	iterations = 10  # The number of times to blink
	interval = .25   # The length of time to blink on or off
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(BUTTONpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(LEDpin, GPIO.OUT)
	x=0
	# The parameters to "range" are inclusive and exclusive, respectively,
	#  so to go from 1 to 10 we have to use 1 and 11 (add 1 to the max)
	#for x in range(1, iterations+1):
	while True:
		x+=1
		#LED stuff
		print("Loop %d: LED on" % (x))
		GPIO.output(LEDpin, GPIO.HIGH)
		time.sleep(interval)
		print("Loop %d: LED off" % (x))
		GPIO.output(LEDpin, GPIO.LOW)
		time.sleep(interval)

		#button stuff
		input_state = GPIO.input(BUTTONpin)
		if input_state == False:
        		print('Button Pressed')
        		time.sleep(0.2)



if __name__ == "__main__":
    main()
