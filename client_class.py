import socket
import time

class ClientError(Exception):
    def __init__(self, text):
        self.text = text

class Client:
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.response = ''
        # створюємо об'єкт сокета та приєднуємся до сервера
        self.sock = socket.socket()
        try:
            self.sock.connect((self.host, self.port))
        except socket.error as err:
            raise ClientError('error connection', err)



    def put(self, key, value, timestamp=None):

        send = ''

        # створюємо рядок для відправки на сервер
        if timestamp == None:
            ts = str(int(time.time()))
            send = 'put' + key + ' ' + str(value) + ' ' + ts + '\n'
        else:
            ts = str(timestamp)
            send = 'put' + key + ' ' + str(value) + ' ' + ts + '\n'

        # відправляємо 'send' на сервер та отримуємо підтвердження
        try:
            self.sock.sendall(send.encode('utf8'))
            self.response = self.sock.recv(1024).decode()
        except socket.error as err:
            raise ClientError('error connection', err)



    def get(self, name):

        name_request = 'get' + ' ' + name + ' ' + '\n'

        # відправляємо запит на сервер та отримуємо відповідь
        try:
            self.sock.sendall(name_request.encode('utf8'))
            self.response = self.sock.recv(1024).decode().split('\n')
        except socket.error as err:
            raise ClientError('error connection', err)

        response_list = self.response[1:len(self.response) - 2]
        response_dict = {}

        if len(response_list) == 0:
            response_dict = {}
        else:
            for i in response_list: # перебираємо список отриманих даних

                ls = i.split(' ')[0] # розбиваємо елемент списку на список та беремо його 1 елемент

                if response_dict.get(ls) == None:
                    ls_tuple = []

                    for item in response_list:
                        if item.split(' ')[0] == ls:
                            ls_tuple.append((int(item.split(' ')[2]), float(item.split(' ')[1]),))

                    ls_tuple.sort(key=lambda x: (x[0], x[1]))
                    response_dict[ls] = ls_tuple

        return response_dict



    def close(self):
        self.sock.close()