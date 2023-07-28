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
    print("Start if __name__ == '__main__'")

    # SERVER = 'localhost'
    SERVER = '10.192.138.231'
    WAITING_PORT = 8765

    message_v = ''


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
        option_key = sys.argv[count]
        if option_key == "-h" and count + 1 < sys_argc:
            count += 1
            hostname_v = sys.argv[count]
        elif option_key == "-p" and count + 1 < sys_argc:
            count += 1
            waiting_port_v = int(sys.argv[count])
        count += 1

    print("Hostname:", hostname_v)
    print("Port:", waiting_port_v)

    data_json = JsonData()
    data_json.connect_socket()
    data_json.send_dht_data()
    data_json.close_socket()

