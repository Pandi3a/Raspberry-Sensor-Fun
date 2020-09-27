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
          
            print "\033[1;33;40m Light \033[0;0m"
         
    else:

            print "\033[1;34;40m Dark \033[0;0m"
            

    time.sleep(5)    
    
    # Sensor Data
    humidity, temperature = Adafruit_DHT.read_retry(11,PIN)
    # Time and Date
    now = datetime.now().strftime('Day: %B %d, %Y Time: %H:%M:%S')
    if humidity is not None and temperature is not None:
        # Output
        print ("------------------------------")
        print now
        print ("------------------------------")
        print("\033[0;31;47m Temp: {0:0.1f} C\033[0;0m \033[0;34;47m Humidity: {1:0.1f} % \033[0;0m".format(temperature, humidity))
        print ("------------------------------")
    else:
        print("\033[1;31;40m Sensor failure. Check wiring.\033[0;0m");
    # Timeout
    time.sleep(10);
