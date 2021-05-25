import socket

def sendable_data(data):
    return str(data).rjust(1024, " ").encode("utf-8")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

num1 = input("Give a number: ")
num2 = input("Give a number: ")

s.sendall(sendable_data(num1))
s.sendall(sendable_data(num2))

msg = s.recv(1024)
print(msg.decode("utf-8"))
