#!/usr/bin/env python3
import sys, socket, threading

# define variables
HOST="127.0.0.1"
PORT=30001
ADDR=(HOST,PORT)
Number_clients=100
addresses = {}
lock=threading.Lock()

def accept_connect_client():
  while True:
      socketclient, socketclient_address=socketserver.accept()
      msg='%s:%s has connected.' % socketclient_address
      print(msg)
      socketclient.send(bytes("Please type your name:","utf8"))
      name=socketclient.recv(4096).decode("utf8")
      socketclient.send(bytes(name,"utf8"))
      socketclient.send(bytes("Please type your room number:  ","utf8"))
      room=socketclient.recv(4096).decode("utf8")
      socketclient.send(bytes(room,"utf8"))

      msg='Welcom {} to room {}.'.format(name,room)
      socketclient.send(bytes(msg,"utf8"))
      with lock:
        addresses[socketclient] = socketclient_address
      handle_client=threading.Thread(target=handle_client, args=[socketclient,name,room],daemon=True)
      handle_client.start()

def handle_client(socketclient,name,room):
  while True:
    msg_rec=socketclient.recv(4096).decode("utf8")
    msg_combine="{}:{}".format(name,msg_rec)
    msg_ready_to_send='{}+{}'.format(msg_combine,room)
    broadcast_msg(msg_ready_to_send)

def broadcast_msg(msg):
    with lock:
          for socket in addresses:
              socket.send(bytes(msg,"utf8"))



socketserver=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketserver.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
socketserver.bind(ADDR)

if __name__ == "__main__":
    socketserver.listen(Number_clients)
    print("Waiting for connection...")
    thread_init = threading.Thread(target=accept_connect_client)
    thread_init.start()
    thread_init.join()

    #bi treo khi 2 connect cung luc
    # while True:
    #   socketclient, socketclient_address=socketserver.accept()
    #   msg='%s:%s has connected.' % socketclient_address
    #   print(msg)
    #   socketclient.send(bytes("Please type your name:","utf8"))
    #   name=socketclient.recv(4096).decode("utf8")
    #   socketclient.send(bytes(name,"utf8"))
    #   socketclient.send(bytes("Please type your room number:  ","utf8"))
    #   room=socketclient.recv(4096).decode("utf8")
    #   socketclient.send(bytes(room,"utf8"))

    #   msg='Welcom {} to room {}.'.format(name,room)
    #   socketclient.send(bytes(msg,"utf8"))
    #   with lock:
    #     addresses[socketclient] = socketclient_address
    #   handle_client=threading.Thread(target=handle_client, args=[socketclient,name,room],daemon=True)
    #   handle_client.start()