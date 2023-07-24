from data_server_PC import csv_read_iterator
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

# data_list = [
#     [35.2, 43.0],
#     [27.5, 32.0],
#     [24.0, 36.0],
#     [18.0, 5.0]
# ]
filename = "./server/csv/csv_datalist.csv"
#filename = 'C:/Users/210503oikawa/Downloads/IoTデバイスプログラミングⅢ/devpro3_G1_sensor/server/csv/csv_datalist.csv'
data_list = csv_read_iterator(filename)

@app.route("/",methods=["GET"])
def top_page():
    
    return render_template('index.html', input_from_python = data_list)

@app.route("/", methods=["POST"])
def top_page2():
    print("Hello! (to Terminal) POST")
    text_from_html_tempe = request.form["new_tempe"]
    text_from_html_humid = request.form["new_humid"]
    print(text_from_html_tempe)
    print(text_from_html_humid)
    try:
        add_tempe = float(text_from_html_tempe)
        if add_tempe < 0 or add_tempe > 50:
            raise ValueError("Temperature value must be between 0 and 50. Please enter a valid numeric value.")
    except ValueError as e:
        if "could not convert string to float" in str(e):
            error_message = "Invalid temperature value. Please enter a valid numeric value."
        else:
            error_message = str(e)
        return render_template("error.html", error_message=error_message)
    try:
        add_humid = float(text_from_html_humid)
        if add_humid < 0 or add_humid > 100:
            raise ValueError("Humidity value must be between 0 and 100. Please enter a valid numeric value.")
    except ValueError as e:
        if "could not convert string to float" in str(e):
            error_message = "Invalid humidity value. Please enter a valid numeric value."
        else:
            error_message = str(e)
        return render_template("error.html", error_message=error_message)
    #add_humid = 0
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