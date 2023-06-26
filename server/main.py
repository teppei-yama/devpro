import data_server_1_PC
import sys
import time
import json
import csv
import datetime
from flask import Flask

app = Flask(__name__)

SERVER = 'localhost'
WAITING_PORT = 8765

LOOP_WAIT = 3

count = 0

@app.route("/hello",methods=["GET"])
def hello_world():
    return "<a href='../'>return top</a>"

@app.route("/",methods=["GET"])
def top_page():
    return f"<a href='/hello'>go to hello</a><p>you visit hello {count} times</p>"


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
            if ("-h" == option_key):
                count = count + 1
                hostname_v = sys.argv[count]

            if ("-p" == option_key):
                count = count + 1
                waiting_port_v = int(sys.argv[count])

            count = count + 1

    #data_server_1_PC.server(hostname_v, waiting_port_v)
    app.run(host = '0.0.0.0', port = 5001 ,debug = True)