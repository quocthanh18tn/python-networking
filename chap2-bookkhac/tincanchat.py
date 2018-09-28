#!/usr/bin/env python3

import socket
HOST = ''
PORT = 4040
def create_listen_socket(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    sock.listen(100)
    return sock
def recv_msg(sock):
    data = bytearray()
    msg = ''
# Repeatedly read 4096 bytes off the socket, storing the bytes
# in data until we see a delimiter
    while not msg:
        recvd = sock.recv(4096)
        if not recvd:
# Socket has been closed prematurely
             raise ConnectionError()
        data = data + recvd
        if b'\0' in recvd:
# we know from our protocol rules that we only send
# one message per connection, so b'\0' will always be
# the last character
            msg = data.rstrip(b'\0')
    msg = msg.decode('utf-8')
    return msg

def prep_msg(msg):
    msg += '\0'
    return msg.encode('utf-8')
def send_msg(sock, msg):
    data = prep_msg(msg)
    sock.sendall(data)

def parse_recvd_data(data):
    parts = data.split(b'\0')
    msgs = parts[:-1]
    rest = parts[-1]
    return (msgs, rest)
def recv_msgs(sock, data=bytes()):
    msgs = []
    while not msgs:
        recvd = sock.recv(4096)
        if not recvd:
            raise ConnectionError()
        data = data + recvd
        (msgs, rest) = parse_recvd_data(data)
        msgs = [msg.decode('utf-8') for msg in msgs]
        return (msgs, rest)