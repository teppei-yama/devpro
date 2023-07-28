#import adafruit_dht
#from board import *
import time
import datetime
import random 

class DHT11:
    def __init__(self):
        #self.instance_dht = adafruit_dht.DHT11(pin=pin, use_pulseio=False)
        self.WAIT_INTERVAL = 10
        self.WAIT_INTERVAL_RETRY = 10

    #def get_dht_data(self):
    #    temp_dht = 200.0  # unnecessary value-setting
    #    humid_dht = 100.0  # unnecessary value-setting
    #    try:
    #        self.instance_dht.measure()
    #        temp_dht = self.instance_dht.temperature
    #        humid_dht = self.instance_dht.humidity

    #    except RuntimeError:
    #        print("RuntimeError: DHT11/22 returns wrong values, maybe.: " + str(datetime.datetime.now()))
    #        raise RuntimeError

    #    except OSError:
    #       print("OSError: DHT11/22: OS Error, but we ignore it.: " + str(datetime.datetime.now()))
    #        raise OSError

    #    return float(temp_dht), float(humid_dht)

    def get_dht_data_for_json(self):
        tempe = 40.0
        humid = 85.0
        count = 0
        data_list = []

        while True:
            try:
                tempe = round(random.uniform(25,35),1) 
                humid = round(random.uniform(55,70),1)
                now_str = str(datetime.datetime.now())
                print("Temperature: %f  Humidity: %f" % (tempe, humid), now_str)            
                data_list.append({'temperature': tempe, 'humidity': humid})
                count = count + 1
                if count > 4:
                    break
                time.sleep(self.WAIT_INTERVAL)
            except RuntimeError:
                print("RuntimeError in get_dht_data(). Let us ignore it!")
                time.sleep(self.WAIT_INTERVAL_RETRY)

            except OSError:
                print("OSError in get_dht_data(). Let us ignore it!")
                time.sleep(self.WAIT_INTERVAL_RETRY)


        return data_list


