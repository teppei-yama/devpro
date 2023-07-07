import data_server_PC
import sys
import time
import json
import csv
import datetime
from flask import Flask,render_template, request

app = Flask(__name__)

SERVER = 'localhost'
WAITING_PORT = 8765

LOOP_WAIT = 3

count = 0

data_list = [
    [35.2, 43.0],
    [27.5, 32.0],
    [24.0, 36.0],
    [18.0, 5.0]
]

@app.route("/",methods=["GET"])
def top_page():
    # data_list = []
    # data_list.append([35.2, 43.0])
    # data_list.append([27.5, 32.0])
    # data_list.append([24.0, 36.0])
    # data_list.append([18.0, 5.0])
    return render_template('index.html', input_from_python = data_list)

@app.route("/", methods=["POST"])
def top_page2():
     print("Hello! (to Terminal) POST")
     text_from_html = request.form["new_tempe"]
     print(text_from_html)
     add_tempe = float(text_from_html)
     add_humid = 0
     #data_list = []
    #  data_list.append([35.2, 43.0])
    #  data_list.append([27.5, 32.0])
    #  data_list.append([24.0, 36.0])
    #  data_list.append([18.0, 5.0])
    #  data_list.append([add_tempe, add_humid])
     data_list.append([add_tempe, add_humid])
     return render_template("index.html",input_from_python = data_list)


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