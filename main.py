import RPi.GPIO as GPIO
import time

def blink(pin=5):
    # Set up the GPIO using BCM pin numbering
    GPIO.setmode(GPIO.BCM)

    # Set up pin 5 as an output pin
    GPIO.setup(pin, GPIO.OUT)

    try:
        while True:
            GPIO.output(pin, GPIO.HIGH)  # Turn on the LED (or whatever is connected)
            time.sleep(1)              # Wait for 1 second
            GPIO.output(pin, GPIO.LOW)   # Turn off the LED
            time.sleep(1)              # Wait for 1 second
    except KeyboardInterrupt:
        # If you press CTRL+C, clean up GPIO pins
        GPIO.cleanup()
    return

def read_LDR(pin=17)
    # Set up GPIO using BCM numbering
    GPIO.setmode(GPIO.BCM)

    # Set up GPIO pin 17 (signal pin) as input
    GPIO.setup(pin, GPIO.IN)

    try:
        while True:
            ldr_value = GPIO.input(pin)  # Read the digital signal from the LDR
            if ldr_value == GPIO.HIGH:
                print("LDR detects high light levels")
            else:
                print("LDR detects low light levels")
            time.sleep(0.3)  # Read every second
    except KeyboardInterrupt:
        GPIO.cleanup()
    return

read_LDR()