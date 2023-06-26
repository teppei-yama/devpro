import adafruit_dht
from board import * 

import time
import datetime
import json
import sys

import sensor

instance_dht = adafruit_dht.DHT11(pin=D4, use_pulseio=False)
WAIT_INTERVAL = 10
WAIT_INTERVAL_RETRY = 5

SERVER = 'localhost'
WAITING_PORT = 8765

if __name__ == '__main__':
    sys_argc = len(sys.argv)
    count = 1
    hostname_v = SERVER
    waiting_port_v = WAITING_PORT
    message_v = ''

    while True:
        print(count, "/", sys_argc)
        if(count >= sys_argc):
            break

        option_key = sys.argv[count]
        #print(option_key)
        if ("-h" == option_key):
            count = count + 1
            hostname_v = sys.argv[count]
            #print(option_key, hostname_v)
        if ("-p" == option_key):
            count = count + 1
            waiting_port_v = int(sys.argv[count])
            #print(option_key, port_v)

        count = count + 1

    print(hostname_v)
    print(waiting_port_v)

    sensor.send_dht_data(hostname_v, waiting_port_v)