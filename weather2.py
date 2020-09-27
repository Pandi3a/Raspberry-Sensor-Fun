# DHT11 libraries
import Adafruit_DHT
import time
from datetime import datetime
import RPi.GPIO as GPIO

# GPIO PIN number
PIN = 17

while True:

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.IN)
    state = GPIO.input(4)


    if (state == 0):
            print "It's Raining!!"
           
    else:
            print "It's Sunny!!"
          

    # Sensor Data
    humidity, temperature = Adafruit_DHT.read_retry(11,PIN)
    # Time and Date
    now = datetime.now().strftime('Day: %B %d, %Y Time: %H:%M:%S')
    if humidity is not None and temperature is not None:
        # Output
        print ("------------------------------")
        print now
        print ("------------------------------")
        print("Temp: {0:0.1f} C Humidity: {1:0.1f} % ".format(temperature, humidity))
        print ("------------------------------")
    else:
        print("Sensor failure. Check wiring.");
    # Timeout
    time.sleep(10);

