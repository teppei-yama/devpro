import adafruit_dht
from board import * 

import time
import datetime
import json

instance_dht = adafruit_dht.DHT11(pin=D4, use_pulseio=False)
WAIT_INTERVAL = 2
WAIT_INTERVAL_RETRY = 5

SERVER = 'localhost'
WAITING_PORT = 8765

def get_dht_data():
    temp_dht = 200.0 # unnecessary value-setting
    humid_dht = 100.0 # unnecessary value-setting
    try:
        instance_dht.measure()
        temp_dht = instance_dht.temperature
        humid_dht = instance_dht.humidity

    except RuntimeError:
        print("RuntimeError: DHT11/22 returns wrong values, maybe.: " + str(datetime.datetime.now()))
        time.sleep(WAIT_INTERVAL_RETRY)
        raise(RuntimeError)
        
    except OSError:
        print("OSError: DHT11/22: OS Error, but we ignore it.: "+ str(datetime.datetime.now()))
        time.sleep(WAIT_INTERVAL_RETRY)
        raise(OSError)

    return float(temp_dht), float(humid_dht)

def send_dht_data(hostname_v1 = SERVER, waiting_port_v1 = WAITING_PORT):
    import socket
    count = 0
    tempe = 40.0
    humid =85.0
    node_s = hostname_v1
    port_s = waiting_port_v1

    try:
        while True:
            try:
                socket_r_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket_r_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                socket_r_s.connect((node_s, port_s))
                tempe, humid = get_dht_data()
                data_list = [{'temperature': tempe, 'humidity': humid}]
                data_json = json.dumps(data_list)
                data_send = data_json.encode('utf-8')
                socket_r_s.send(data_send)
                print(data_json)
                print("data", type(data_json))

            except RuntimeError:
                print("RuntimeError in get_dht_data()")
                time.sleep(WAIT_INTERVAL_RETRY)
            except OSError:
                print("OSError in get_dht_data()")
                time.sleep(WAIT_INTERVAL_RETRY)

            socket_r_s.close()
            time.sleep(WAIT_INTERVAL)
            count = count + 1
            if(count > 5):
                break
    
    except KeyboardInterrupt:
        print("code is interrupted!")

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

    send_dht_data(hostname_v, waiting_port_v)