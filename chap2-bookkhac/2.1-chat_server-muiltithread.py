#!/usr/bin/env python3

import threading, queue
import tincanchat

HOST = tincanchat.HOST
PORT = tincanchat.PORT
send_queues = {}
lock = threading.Lock()


## xu ly ham nhan
def handle_client_recv(sock, addr,name,room):
  rest = bytes()
  while True:
    try:
          (msgs, rest) = tincanchat.recv_msgs(sock, rest)
    except (EOFError, ConnectionError):
          handle_disconnect(sock, addr)
          break
    for msg in msgs:
          msg = '{}: {}'.format(name, msg)   #dinh dang ten: noi dung tn
          print(msg)
          msg1='{}+{}'.format(msg,room)   #dinh dang them room de chat rieng
          broadcast_msg(msg1)

##xu ly send toi tat ca client co chung room
def handle_client_send(sock, q, addr):
    while True:
          msg = q.get()
          if msg == None: break
          try:
                  tincanchat.send_msg(sock, msg)
          except (ConnectionError, BrokenPipe):
                  handle_disconnect(sock, addr)
                  break

##xu ly broadcast, ung voi moi queue cua socket client rieng biet
## ta dua goi tin msg vao queue
## ham send se block cho toi khi queue co data vao

def broadcast_msg(msg):
    with lock:
          for q in send_queues.values():
              q.put(msg)
def handle_disconnect(sock, addr):
    fd = sock.fileno()
    q = send_queues.get(fd, None)
    if q:
              q.put(None)
              del send_queues[fd]
              addr = sock.getpeername()
              print('Client {} disconnected'.format(addr))
              sock.close()

if __name__ == '__main__':
        listen_sock = tincanchat.create_listen_socket(HOST, PORT)
        addr = listen_sock.getsockname()
        while True:
                  client_sock,addr = listen_sock.accept()
                  rest = bytes()    ## nhan goi ten xac dinh ten
                  (msgs, rest) = tincanchat.recv_msgs(client_sock, rest)
                  name=msgs

                  rest = bytes()   ## nhan goi tin xac dinh so phong
                  (msgs, rest) = tincanchat.recv_msgs(client_sock, rest)
                  room=msgs
                  q = queue.Queue()
                  with lock:
                        send_queues[client_sock.fileno()] = q
                  recv_thread = threading.Thread(target=handle_client_recv,args=[client_sock, addr,name,room],daemon=True)
                  send_thread = threading.Thread(target=handle_client_send,args=[client_sock, q,addr],daemon=True)
                  recv_thread.start()
                  send_thread.start()
                  print('Connection from {}'.format(addr))