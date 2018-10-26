#!/usr/bin/env python3
import sys, socket, threading
import tincanchat
import argparse

HOST = sys.argv[-1] if len(sys.argv) > 1 else '127.0.0.1'
PORT = tincanchat.PORT
def handle_input(sock):
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
      # parser = argparse.ArgumentParser()
      # parser.add_argument('name', help="display a square of a given number")
      # parser.add_argument('port',help="display a square of a given number",type=int)
      # given_args = parser.parse_args()
      # name = given_args.name
      # port1 = given_args.port
      # print(port1)
      # print(name)
      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      sock.connect((HOST, PORT))
      print('Connected to {}:{}'.format(HOST, PORT))
      msg=input()
      tincanchat.send_msg(sock, msg)
      msg=input()
      tincanchat.send_msg(sock, msg)
# Create thread for handling user input and message sending
      thread = threading.Thread(target=handle_input,args=[sock],daemon=True)
      thread.start()
      rest = bytes()
      addr = sock.getsockname()
# Loop indefinitely to receive messages from server
      while True:
          try:
      # blocks
              (msgs, rest) = tincanchat.recv_msgs(sock, rest)
              for msg in msgs:
                  print(msg)
          except ConnectionError:
              print('Connection to server closed')
              sock.close()
              break