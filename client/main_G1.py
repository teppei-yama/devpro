from json_data import JsonData
import sys

if __name__ == '__main__':
    print("Start if __name__ == '__main__'")

    SERVER = 'localhost'
    #SERVER = '10.192.138.231'
    WAITING_PORT = 8765

    sys_argc = len(sys.argv)
    count = 1
    hostname_v = SERVER
    waiting_port_v = WAITING_PORT

    while True:
        print(count, "/", sys_argc)
        if(count >= sys_argc):
            break
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
    while True:
        data_json = JsonData()
        data_json.connect_socket()
        data_json.send_dht_data()
        data_json.close_socket()