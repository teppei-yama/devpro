from json_data import JsonData
if __name__ == '__main__':
    print("Start if __name__ == '__main__'")
    data_sender = JsonData()
    data_sender.connect_socket()
    data_sender.send_dht_data()
    data_sender.close_socket()