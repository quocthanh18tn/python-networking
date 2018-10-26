#!/usr/bin/env python3
import sys, socket, threading
import tincanchat
import argparse

HOST = sys.argv[-1] if len(sys.argv) > 1 else '127.0.0.1'
PORT = tincanchat.PORT
def handle_input(sock,name,room):
    print("Chao mung {} vao phong {}".format(name,room))
    print("Type messages, enter to send. 'q' to quit")
    while True:
        msg = input() # Blocks
        if msg == 'q':
              sock.shutdown(socket.SHUT_RDWR)
              sock.close()
              break
        try:
              tincanchat.send_msg(sock, msg) # Blocks until sent
        except (BrokenPipeError, ConnectionError):
              break
if __name__ == '__main__':
      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      sock.connect((HOST, PORT))
      print('Connected to {}:{}'.format(HOST, PORT))
      print('Moi ban nhap ten:')
      msg=input()
      tincanchat.send_msg(sock, msg)
      name=msg
      print('Moi ban nhap ma so phong:')
      msg=input()
      tincanchat.send_msg(sock, msg)
      room=msg
# Create thread for handling user input and message sending
      thread = threading.Thread(target=handle_input,args=[sock,name,room],daemon=True)
      thread.start()
      rest = bytes()
      addr = sock.getsockname()
# Loop indefinitely to receive messages from server
      while True:
          try:
      # blocks
              (msgs, rest) = tincanchat.recv_msgs(sock, rest)
              for msg in msgs:
                parts1 = msg.split('+')
                check=(parts1[-1])
                check=check.strip("[")
                check=check.strip("]")
                check=check.strip("'")
                if (check ==room):
                    strmsg=''.join(parts1[:-1])
                    print(strmsg)

          except ConnectionError:
              print('Connection to server closed')
              sock.close()
              break