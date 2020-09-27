#!/usr/bin/env python
# DHT11 libraries
import Adafruit_DHT
import time
from datetime import datetime

# GPIO PIN number
PIN = 17

while True:
    # Sensor Data
    humidity, temperature = Adafruit_DHT.read_retry(11,PIN)
    # Time and Date
    now = datetime.now().strftime('Day: %B %d, %Y Time: %H:%M:%S')
    if humidity is not None and temperature is not None:
        # Output
        print now
        print ("------------------------------")
        print("\033[0;31;47m Temp: {0:0.1f} C\033[0;0m \033[0;34;47m Humidity: {1:0.1f} % \033[0;0m".format(temperature, humidity))
        print ("------------------------------")
    else:
        print("Sensor failure. Check wiring.");
    # Timeout
    time.sleep(10);

