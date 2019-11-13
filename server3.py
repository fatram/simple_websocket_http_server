from WebsocketServer import WebsocketServer
import hashlib

this_file_group_binary_data = open('tubes2jarkom.zip', 'rb').read()

# To check md5 checksum of a binary data
def checkmd5(bindat):
    m = hashlib.md5()
    if(isinstance(bindat, str)):
        m.update(bindat.encode())
    else:
        m.update(bindat)
    return m.hexdigest()

# Called for every client connecting (after handshake)
def new_client(client, server):
	print("New client connected and was given id %d" % client['id'])
	# server.send_message_to_all("Hey all, a new client has joined us")


# Called for every client disconnecting
def client_left(client, server):
	print("Client(%d) disconnected" % client['id'])


# Called when a client sends a message
def message_received(client, server, message):
    print("Client(%d) said: %s..." % (client['id'], message[0:100]))
    if(message[0:6] == "!echo "):
        server.send_message(client, message[6:])
    elif(message == "!submission"):
        server.send_message(client, this_file_group_binary_data)
    else:
        if(checkmd5(message).lower() == checkmd5(this_file_group_binary_data).lower()):
            server.send_message(client, "1")
        else:
            server.send_message(client, "0")



PORT=8765
server = WebsocketServer(PORT)
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(message_received)
server.run_forever()