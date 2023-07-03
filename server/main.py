import data_server_1_PC
import sys
import time
import json
import csv
import datetime
from flask import Flask,render_template

app = Flask(__name__)

SERVER = 'localhost'
WAITING_PORT = 8765

LOOP_WAIT = 3

count = 0

@app.route("/",methods=["GET"])
def top_page():
    return render_template('index.html')


def index():
    with open("datalist.csv") as f:
        data_list = []
        all_data_iter = csv.reader(f)
        for row in all_data_iter:
            data_list.append(row)
    return render_template("index.html", input_from_python = data_list)


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