#!/usr/bin/env /usr/bin/python3
# -*- coding: utf-8 -*-

# Sample Implemantation of IPUT Course IoT Device Programming 3 (2023 Summer)
# Week 04
#
# Socket Server (Multi-Thread) WITH BLANK

# May 1, 2023
# Michiharu Takemoto (takemoto.development@gmail.com)

#
# NOT MIT License
#

import sys
import time

#SERVER = 'localhost'
SERVER = '127.0.0.1'
WAITING_PORT = 8765
KEY_ID = 'takemoto'

LOOP_INTERVAL = 5

def server_test(server_v1=SERVER, waiting_port_v1=WAITING_PORT):
    import socket
    import threading
    
    def recv_data1024(socket1, client_address1):
        data_r = socket1.recv(1024)
        data_r_str = data_r.decode('utf-8')
        # data_r_json = pickle.loads(data_r)
        # data_r_list = json.loads(data_r_json)
        # data_r_str = str(data_r_list)
        print('I (the server) have just received the data __'
            + data_r_str + '__ from the client. '
            + str(client_address1))

        time.sleep(LOOP_INTERVAL)

        print("Now, closing the data socket.")
        socket1.XXXX()


    # socoket for waiting of the requests.
    # AF_INET     : IPv4
    # SOCK_STREAM : TCP
    socket_w = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    socket_w.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    node_s = server_v1
    port_s = waiting_port_v1
    socket_w.XXXX((node_s, port_s)) 

    BACKLOG = 5
    socket_w.XXXX(BACKLOG)

    print('Waiting for the connection from the client(s). '
        + 'node: ' + node_s + '  '
        + 'port: ' + str(port_s))

    try:
        while True:
            socket_s_r, client_address = socket_w.accept()
            print('Connection from ' 
                + str(client_address) 
                + " has been established.")

            thread = threading.Thread(target=recv_data1024, 
                args=(socket_s_r, client_address))
            thread.start()

    except KeyboardInterrupt:
        print("Ctrl-C is hit!")
        print("Now, closing the waiting socket.")
        socket_s_r.XXXX()

if __name__ == '__main__':
    print("Start if __name__ == '__main__'")

    sys_argc = len(sys.argv)
    count = 1
    hostname_v = SERVER
    waiting_port_v = WAITING_PORT
    key_id_v = KEY_ID


    while True:
            print(count, "/", sys_argc)
            if(count >= sys_argc):
                break

            option_key = sys.argv[count]
#            print(option_key)
            if ("-h" == option_key):
                count = count + 1
                hostname_v = sys.argv[count]
#                print(option_key, hostname_v)

            if ("-p" == option_key):
                count = count + 1
                waiting_port_v = int(sys.argv[count])
#               print(option_key, waiting_port_v)

            if ("-k" == option_key):
                count = count + 1
                key_id_v = sys.argv[count]
#                print(option_key, key_id_v)

            count = count + 1

    print(hostname_v)
    print(waiting_port_v)
    
    server_test(hostname_v, waiting_port_v)
