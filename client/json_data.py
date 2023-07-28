import json
import socket
from dht_class import DHT11

class JsonData:
    def __init__(self):
        self.dht = DHT11()
        self.socket_r_s = None
        self.node_s = 'localhost'
        self.port_s = 8765
        print("Hostname:", self.node_s)
        print("Port:", self.port_s)



    def connect_socket(self):
        self.socket_r_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_r_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket_r_s.connect((self.node_s, self.port_s))

    def close_socket(self):
        if self.socket_r_s:
            self.socket_r_s.close()

    def get_json_data(self):
        data_list = self.dht.get_dht_data_for_json()
        data_json = json.dumps(data_list)
        print(data_json)
        print("data", type(data_json))
        return data_json

    def send_dht_data(self):
        data_json = self.get_json_data()
        data_send = data_json.encode('utf-8')
        self.socket_r_s.send(data_send)




