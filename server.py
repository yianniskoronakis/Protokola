import socket

HOST = "127.0.0.1"
PORT = 1234


def sendable_data(data):
    return str(data).rjust(1024, " ").encode("utf-8")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print("Connected by", addr)
        data = conn.recv(1024)
        data2 = conn.recv(1024)
        if (int(data)>=0 and int(data)<=30000) and (int(data2)>=0 and int(data2)<=30000) and int(data2)!=0:
            print(data.decode("utf-8").strip())
            print(data2.decode("utf-8").strip())

            a = int(data2.decode("utf-8").strip())
            b = int(data.decode("utf-8").strip())
            conn.send(sendable_data(a + b))
            conn.send(sendable_data(a - b))
            conn.send(sendable_data(a * b))
            conn.send(sendable_data(a / b))
        if int(data2) == 0:
            conn.send(sendable_data("number 2 is 0"))
        if not(int(data)>=0 and int(data)<=30000):
            conn.send(sendable_data("number 1 is out of range"))
        if not(int(data2)>=0 and int(data2)<=30000):
            conn.send(sendable_data("number 2 is out of range"))
