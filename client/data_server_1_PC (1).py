#!/usr/bin/env /usr/bin/python3
# -*- coding: utf-8 -*-

# Sample Implemantation of IPUT Course IoT Device Programming 3 (2023 Summer)
# Week 04
#
# Socket Server (Too simple to work correctly) WITH BLANK

# May 1, 2023
# Michiharu Takemoto (takemoto.development@gmail.com)

#
# NOT MIT License
#

import sys
import time
import json
import csv
import datetime


SERVER = 'localhost'
#SERVER = '127.0.0.1'
WAITING_PORT = 8765

LOOP_WAIT = 3

#DATA_DIR = '/home/pi/devpro3/data'
DATA_DIR = r'C:\Users\IPUT shunpei kojima\OneDrive - nkz.ac.jp\ドキュメント\devpro3\csv_datalist'  #csv_datalistというフォルダをdevpro3の下に置くことで実行時にファイルがcsv_datalistの中にまとめられる。
CSV_DATANAME = 'csv_datalist'
now = datetime.datetime.now()
time_str = now.strftime("%Y-%m-%d-%H-%M-%S")
filename = f"{DATA_DIR}/{CSV_DATANAME}_{time_str}.csv"

def csv_write(data_list_list):
    with open(filename, mode='a') as f:
        for row in data_list_list:
            data1 = row['temperature']
            data2 = row['humidity']
            row_str = str(data1) + ',' + str(data2)
            f.write(row_str)
            f.write('\n')

def csv_read_iterator():
    with open(filename) as f:
        all_data_iter = csv.reader(f)
        for row in all_data_iter:
            print(row)

def server_test(server_v1=SERVER, waiting_port_v1=WAITING_PORT):
    import socket
    
    # socoket for waiting of the requests.
    # AF_INET     : IPv4
    # SOCK_STREAM : TCP
    socket_w = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    socket_w.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    node_s = server_v1
    port_s = waiting_port_v1
    socket_w.bind((node_s, port_s)) 

    BACKLOG = 5
    socket_w.listen(BACKLOG)

    print('Waiting for the connection from the client(s). '
        + 'node: ' + node_s + '  '
        + 'port: ' + str(port_s))

    try:
        while True:
            socket_s_r, client_address = socket_w.accept()
            print('Connection from ' 
                + str(client_address) 
                + " has been established.")

            data_r = socket_s_r.recv(1024)
            data_r_str = data_r.decode('utf-8')
            data_r_list = json.loads(data_r_str)
            print('I (the server) have just received the data __'
                + data_r_str + '__ from the client. '
                + str(client_address))
            print(type(data_r_list))
            
            csv_write(data_r_list)
            csv_read_iterator()


            time.sleep(LOOP_WAIT)

            print("Now, closing the data socket.")
            socket_s_r.close()

    except KeyboardInterrupt:
        print("Ctrl-C is hit!")
        print("Now, closing the data socket.")
        socket_s_r.close()
        print("Now, closing the waiting socket.")
        socket_w.close()

if __name__ == '__main__':
    print("Start if __name__ == '__main__'")

    sys_argc = len(sys.argv)
    count = 1
    hostname_v = SERVER
    waiting_port_v = WAITING_PORT

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

            count = count + 1

    print(hostname_v)
    print(waiting_port_v)
    
    server_test(hostname_v, waiting_port_v)
