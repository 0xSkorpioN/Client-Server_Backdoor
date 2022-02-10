import socket

SRV_ADDR = input("Enter the Server Address: ")
SRV_PORT = int(input("Enter the Server Port: "))

def print_menu():

    print("################################")
    print("## 1- Get System Info         ##")
    print("## 2- List Directory Content  ##")
    print("## 3- Close the Connection    ##")
    print ("################################")


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SRV_ADDR, SRV_PORT))

print("Connection Established")

print_menu()

while 1:

    message = input("Enter an option: ")

    if(message == "1"):

        s.sendall(message.encode())
        data = s.recv(1024)
        if not data:
            break
        print(data.decode('utf-8'))

    elif(message == "2"):

        path = input("Enter the Path: ")
        s.sendall (message.encode ( ))
        s.sendall (path.encode ( ))
        data = s.recv (1024)
        data = data.decode ('utf-8').split(",")
        print("*" * 30)
        for x in data:
            print(x)
        print("*" * 30)

    elif (message == "3"):

        s.sendall (message.encode ( ))
        s.close()

    print_menu()

