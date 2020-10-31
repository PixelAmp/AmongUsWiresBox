import RPi.GPIO as GPIO
import time

def successSequence(LEDpins, GPIO):
    interval = .25
    while interval > 0:
        GPIO.output(LEDpins[0], GPIO.HIGH)
        time.sleep(interval)
        GPIO.output(LEDpins[1], GPIO.HIGH)
        time.sleep(interval)
        GPIO.output(LEDpins[2], GPIO.HIGH)
        time.sleep(interval)
        GPIO.output(LEDpins[3], GPIO.HIGH)
        time.sleep(interval)

        GPIO.output(LEDpins[0], GPIO.LOW)
        time.sleep(interval)
        GPIO.output(LEDpins[1], GPIO.LOW)
        time.sleep(interval)
        GPIO.output(LEDpins[2], GPIO.LOW)
        time.sleep(interval)
        GPIO.output(LEDpins[3], GPIO.LOW)
        time.sleep(interval)

        interval -= .05
    
    return

def startupSequence(LEDpins, GPIO):

    GPIO.output(LEDpins[0], GPIO.HIGH)
    GPIO.output(LEDpins[1], GPIO.HIGH)
    GPIO.output(LEDpins[2], GPIO.HIGH)
    GPIO.output(LEDpins[3], GPIO.HIGH)
    time.sleep(1)

    GPIO.output(LEDpins[0], GPIO.LOW)
    GPIO.output(LEDpins[1], GPIO.LOW)
    GPIO.output(LEDpins[2], GPIO.LOW)
    GPIO.output(LEDpins[3], GPIO.LOW)
    time.sleep(.5)

    successSequence(LEDpins, GPIO)

    GPIO.output(LEDpins[0], GPIO.HIGH)
    GPIO.output(LEDpins[1], GPIO.HIGH)
    GPIO.output(LEDpins[2], GPIO.HIGH)
    GPIO.output(LEDpins[3], GPIO.HIGH)
    time.sleep(1)

    GPIO.output(LEDpins[0], GPIO.LOW)
    time.sleep(.1)
    GPIO.output(LEDpins[1], GPIO.LOW)
    time.sleep(.1)
    GPIO.output(LEDpins[2], GPIO.LOW)
    time.sleep(.1)
    GPIO.output(LEDpins[3], GPIO.LOW)
    time.sleep(1.1)

    print("Startup successful!")
    return


def main():
    print("Starting!")
    LEDpins = [5,13,21,25]      # The Pins for LED's
    BUTTONpins = [22,21,17,4]    # The The Pins for the wires

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    GPIO.setup(LEDpins[0], GPIO.OUT)
    GPIO.setup(BUTTONpins[0], GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(LEDpins[1], GPIO.OUT)
    GPIO.setup(BUTTONpins[1], GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(LEDpins[2], GPIO.OUT)
    GPIO.setup(BUTTONpins[2], GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(LEDpins[3], GPIO.OUT)
    GPIO.setup(BUTTONpins[4], GPIO.IN, pull_up_down=GPIO.PUD_UP)

    startupSequence(LEDpins, GPIO)

    while True:
        if GPIO.input(BUTTONpins[0]) == False:
            GPIO.output(LEDpins[0], GPIO.HIGH)
        else:
            GPIO.output(LEDpins[0], GPIO.LOW)

        if GPIO.input(BUTTONpins[1]) == False:
            GPIO.output(LEDpins[1], GPIO.HIGH)
        else:
            GPIO.output(LEDpins[1], GPIO.LOW)

        if GPIO.input(BUTTONpins[2]) == False:
            GPIO.output(LEDpins[2], GPIO.HIGH)
        else:
            GPIO.output(LEDpins[2], GPIO.LOW)

        if GPIO.input(BUTTONpins[3]) == False:
            GPIO.output(LEDpins[3], GPIO.HIGH)
        else:
            GPIO.output(LEDpins[3], GPIO.LOW)

        if not GPIO.input(BUTTONpins[0]) and not GPIO.input(BUTTONpins[1]) and not GPIO.input(BUTTONpins[2]) and not GPIO.input(BUTTONpins[3]):
            time.sleep(.5)
            successSequence(LEDpins, GPIO)

if __name__ == "__main__":
    main()
