import socket

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    clientsocket.send(bytes("welcome to the server!", "utf-8"))
    with clientsocket:
        num1=clientsocket.recv(1024)
        num2=clientsocket.recv(1024)
        num1=int(num1.decode("utf-8").strip())
        num2=int(num2.decode("utf-8").strip())
        sum=num1+num2
        mul=num1*num2
        sub=num1-num2
        div=num1/num2
        clientsocket.sendall(sum)
