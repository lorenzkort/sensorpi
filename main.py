import RPi.GPIO as GPIO
import time

# Set up the GPIO using BCM pin numbering
GPIO.setmode(GPIO.BCM)

# Set up pin 5 as an output pin
GPIO.setup(5, GPIO.OUT)

try:
    while True:
        GPIO.output(5, GPIO.HIGH)  # Turn on the LED (or whatever is connected)
        time.sleep(1)              # Wait for 1 second
        GPIO.output(5, GPIO.LOW)   # Turn off the LED
        time.sleep(1)              # Wait for 1 second
except KeyboardInterrupt:
    # If you press CTRL+C, clean up GPIO pins
    GPIO.cleanup()
