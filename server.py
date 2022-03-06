import socket
import threading

HOST = '127.0.0.1'
PORT = 8000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()

clients = []
nicknames = []


# we want to do many things at once -> so multithread

# broadcast -> send received msg to all the messangers (clients)
def broadcast(msg):
    for client in clients:
        client.send(msg)

# handle -> handling conneted clients
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            # this will be printed on the server console logs
            print(f"{nicknames[clients.index(client)]}")
            # broadcast will send the message to all clinets
            broadcast(message)
        except:
            # get the position of the client to remove it
            index = clients.index(client)
            clients.remove(client)
            client.close()
            # get the nickname of the client to remove it
            nickname = nicknames[index]
            nicknames.remove(nickname)
            # break will automatically stops the thread
            break


# receive -> accept new connections with clients, in main thread
def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with: {str(address)}")
        client.send("NICK".encode("utf-8"))
        nickname = client.recv(1024)

        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is: {nickname}")
        broadcast(f"{nickname} connected to the server!\n ".encode("utf-8"))
        client.send("Connected to the server".encode("utf-8"))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("server is running")
receive()

