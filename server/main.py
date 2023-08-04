import data_server_PC
import sys
import time
import json
import csv
import datetime
from flask import Flask,render_template, request
import threading
app = Flask(__name__)

SERVER = 'localhost'
WAITING_PORT = 8765

LOOP_WAIT = 3

count = 0

filename = "./csv/csv_datalist.csv"


@app.route("/",methods=["GET"])
def top_page():
    get_dt = datetime.datetime.now().replace(second=0, microsecond=0)
    data_list = data_server_PC.csv_read_iterator(filename)
    return render_template('index.html', get_date = get_dt,input_from_python = data_list)

@app.route("/", methods=["POST"])
def top_page2():
    print("Hello! (to Terminal) POST")
    text_from_html_tempe = request.form["new_tempe"]
    text_from_html_humid = request.form["new_humid"]
    print(text_from_html_tempe)
    print(text_from_html_humid)
    get_dt = datetime.datetime.now().replace(second=0, microsecond=0)
    try:
        add_tempe = float(text_from_html_tempe)
        if add_tempe < -20 or add_tempe > 60:
            raise ValueError("Temperature value must be between 0 and 50. Please enter a valid numeric value.")
    except ValueError as e:
        if "could not convert string to float" in str(e):
            error_message = "Invalid temperature value. Please enter a valid numeric value."
        else:
            error_message = str(e)
        return render_template("error.html", error_message=error_message)
    try:
        add_humid = float(text_from_html_humid)
        if add_humid < 5 or add_humid > 95:
            raise ValueError("Humidity value must be between 0 and 100. Please enter a valid numeric value.")
    except ValueError as e:
        if "could not convert string to float" in str(e):
            error_message = "Invalid humidity value. Please enter a valid numeric value."
        else:
            error_message = str(e)
        return render_template("error.html", error_message=error_message)
    #add_humid = 0
    data_list.append([add_tempe, add_humid])
    return render_template("index.html",get_date = get_dt, input_from_python = data_list)


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

    thread = threading.Thread(target=data_server_PC.server,args=(hostname_v, waiting_port_v))
    thread.start()
    app.run(host = '0.0.0.0', port = 5001 ,debug = True)