import RPi.GPIO as GPIO
import time

def Standalone(LEDpins, BUTTONpins, interval):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    for slot in range(4):
        GPIO.setup(LEDpins[slot], GPIO.OUT)
        GPIO.setup(BUTTONpins[slot], GPIO.IN, pull_up_down=GPIO.PUD_UP)
    while True:
        #LED stuff
        GPIO.output(LEDpins[0], GPIO.HIGH)
        GPIO.output(LEDpins[1], GPIO.HIGH)
        GPIO.output(LEDpins[2], GPIO.HIGH)
        GPIO.output(LEDpins[3], GPIO.HIGH)
        time.sleep(interval)
        
        GPIO.output(LEDpins[0], GPIO.LOW)
        GPIO.output(LEDpins[1], GPIO.LOW)
        GPIO.output(LEDpins[2], GPIO.LOW)
        GPIO.output(LEDpins[3], GPIO.LOW)
        time.sleep(interval)

        #button stuff
        cable0 = GPIO.input(BUTTONpins[0])
        cable1 = GPIO.input(BUTTONpins[1])
        cable2 = GPIO.input(BUTTONpins[2])
        cable3 = GPIO.input(BUTTONpins[3])
        if cable0 == False:
            print('Cable 0 connected')
        if cable1 == False:
            print('Cable 1 connected')
        if cable2 == False:
            print('Cable 2 connected')
        if cable3 == False:
            print('Cable 3 connected')
        
        time.sleep(interval)


def CablesLightLEDs(LEDpins, BUTTONpins, interval):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    for slot in range(4):
        GPIO.setup(LEDpins[slot], GPIO.OUT)
        GPIO.setup(BUTTONpins[slot], GPIO.IN, pull_up_down=GPIO.PUD_UP)
    while True:
        cable0 = GPIO.input(BUTTONpins[0])
        cable1 = GPIO.input(BUTTONpins[1])
        cable2 = GPIO.input(BUTTONpins[2])
        cable3 = GPIO.input(BUTTONpins[3])
        
        
        GPIO.output(LEDpins[0], GPIO.HIGH) if cable0 == False else GPIO.output(LEDpins[0], GPIO.LOW)
        GPIO.output(LEDpins[1], GPIO.HIGH) if cable0 == False else GPIO.output(LEDpins[1], GPIO.LOW)
        GPIO.output(LEDpins[2], GPIO.HIGH) if cable0 == False else GPIO.output(LEDpins[2], GPIO.LOW)
        GPIO.output(LEDpins[3], GPIO.HIGH) if cable0 == False else GPIO.output(LEDpins[3], GPIO.LOW)

def cleanLoop(LEDpins, BUTTONpins, interval):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    for slot in range(4):
        GPIO.setup(LEDpins[slot], GPIO.OUT)
        GPIO.setup(BUTTONpins[slot], GPIO.IN, pull_up_down=GPIO.PUD_UP)
    for slot in range(4):
        cable = GPIO.input(BUTTONpins[slot])
        GPIO.output(LEDpins[slot], GPIO.HIGH) if cable == False else GPIO.output(LEDpins[slot], GPIO.LOW)



def main():
    LEDpins = [4,17.27,22]      # The pins for LED's
    BUTTONpins = [5,6,13,19]    # The The Pins for the wires
    interval = .2               # The length of time to blink on or off
    
    # GPIO.setmode(GPIO.BCM)
    # GPIO.setwarnings(False)
    # for slot in range(4):
    #     GPIO.setup(LEDpins[slot], GPIO.OUT)
    #     GPIO.setup(BUTTONpins[slot], GPIO.IN, pull_up_down=GPIO.PUD_UP)

    Standalone(LEDpins, BUTTONpins, interval)
    #CablesLightLEDs(LEDpins, BUTTONpins, interval)
    #cleanLoop(LEDpins, BUTTONpins, interval)





if __name__ == "__main__":
    main()