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
    for slot in range(4):
        GPIO.setup(LEDpins[slot], GPIO.OUT)
        GPIO.setup(BUTTONpins[slot], GPIO.IN, pull_up_down=GPIO.PUD_UP)

    startupSequence(LEDpins, GPIO)
    
    GPIO.output(LEDpins[0], GPIO.LOW)
    GPIO.output(LEDpins[1], GPIO.LOW)
    GPIO.output(LEDpins[2], GPIO.LOW)
    GPIO.output(LEDpins[3], GPIO.LOW)

    while True:
        for slot in range(4):
            cable = GPIO.input(BUTTONpins[slot])
            GPIO.output(LEDpins[slot], GPIO.HIGH) if cable == True else GPIO.output(LEDpins[slot], GPIO.LOW)

            if GPIO.output(LEDpins[0], GPIO.HIGH) and GPIO.output(LEDpins[1], GPIO.HIGH) and GPIO.output(LEDpins[2], GPIO.HIGH) and GPIO.output(LEDpins[3], GPIO.HIGH):
                time.sleep(.5)
                successSequence(LEDpins, GPIO)

if __name__ == "__main__":
    main()
