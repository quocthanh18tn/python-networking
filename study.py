#!/usr/bin/env python

#---------------------------------Printing your machine's name andIPv4 address
# import socket
# def print_machine_info():
#     host_name = socket.gethostname()
#     ip_address = socket.gethostbyname(host_name)
#     print "Host name: %s" % host_name
#     print "IP address: %s" % ip_address
# if __name__ == '__main__':
#     print_machine_info()

    #output
    # Host name: QuocThanh
    # IP address: 127.0.1.1

# ----------------------------------------------------------Retrieving a remote machine's IP address
# import socket
# def get_remote_machine_info():
#   remote_host = 'www.python.org'
#   try:
#     print "IP address: %s" %socket.gethostbyname(remote_host)
#   except socket.error, err_msg:
#     print "%s: %s" %(remote_host, err_msg)
# if __name__ == '__main__':
#   get_remote_machine_info()

#   output
#   IP address: 151.101.0.223

# ----------------------------------------------------------Converting an IPv4 address to differentformats
# import socket
# from binascii import hexlify
# def convert_ip4_address():
#   for ip_addr in ['127.0.0.1', '192.168.0.1']:
#     packed_ip_addr = socket.inet_aton(ip_addr)
#     unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)
#     print "IP Address: %s => Packed: %s, Unpacked: %s"%(ip_addr, hexlify(packed_ip_addr), unpacked_ip_addr)
# if __name__ == '__main__':
#     convert_ip4_address()

# output
# IP Address: 127.0.0.1 => Packed: 7f000001, Unpacked: 127.0.0.1
# IP Address: 192.168.0.1 => Packed: c0a80001, Unpacked: 192.168.0.1


# ----------------------------------------------------------Finding a service name, given the port and protocol

# import socket
# def find_service_name():
#   protocolname = 'tcp'
#   for port in [80, 25]:
#     print "Port: %s => service name: %s" %(port, socket.getservbyport(port, protocolname))
#   print "Port: %s => service name: %s" %(53, socket.getservbyport(53, 'udp'))
# if __name__ == '__main__':
#   find_service_name()

# output
# Port: 80 => service name: http
# Port: 25 => service name: smtp
# Port: 53 => service name: domain


# ----------------------------------------------------------Converting integers to and from host to network byte order
# import socket
# def convert_integer():
#   data = 1234
# # 32-bit
#   print "Original: %s => Long host byte order: %s, Network byteorder: %s"%(data, socket.ntohl(data), socket.htonl(data))
# # 16-bit
#   print "Original: %s => Short host byte order: %s, Network byteorder: %s"%(data, socket.ntohs(data), socket.htons(data))
# if __name__ == '__main__':
#   convert_integer()

#   output
#   Original: 1234 => Long host byte order: 3523477504, Network byteorder: 3523477504
#   Original: 1234 => Short host byte order: 53764, Network byteorder: 53764

# ----------------------------------------------------------Setting and getting the default socket timeout

# import socket
# def test_socket_timeout():
#   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#   print "Default socket timeout: %s" %s.gettimeout()
#   s.settimeout(100)
#   print "Current socket timeout: %s" %s.gettimeout()
# if __name__ == '__main__':
#   test_socket_timeout()

#   output
#   Default socket timeout: None
#   Current socket timeout: 100.0

# ----------------------------------------------------------Handling socket errors gracefully
# import sys
# import socket
# import argparse
# def main():
# # setup argument parsing
#   parser = argparse.ArgumentParser(description='Socket ErrorExamples')
#   parser.add_argument('--host', action="store", dest="host",required=False)
#   parser.add_argument('--port', action="store", dest="port",type=int, required=False)
#   parser.add_argument('--file', action="store", dest="file",required=False)
#   given_args = parser.parse_args()
#   host = given_args.host
#   port = given_args.port
#   filename = given_args.file
#   # First try-except block -- create socket
#   try:
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#   except socket.error, e:
#     print "Error creating socket: %s" % e
#     sys.exit(1)
# # Second try-except block -- connect to given host/port
#   try:
#     s.connect((host, port))
#   except socket.gaierror, e:
#     print "Address-related error connecting to server: %s" % e
#     sys.exit(1)
#   except socket.error, e:
#     print "Connection error: %s" % e
#     sys.exit(1)
#   # Third try-except block -- sending data
#   try:
#     s.sendall("GET %s HTTP/1.0\r\n\r\n" % filename)
#   except socket.error, e:
#     print "Error sending data: %s" % e
#     sys.exit(1)
#   while 1:
#   # Fourth tr-except block -- waiting to receive data fromremote host
#     try:
#       buf = s.recv(2048)
#     except socket.error, e:
#       print "Error receiving data: %s" % e
#       sys.exit(1)
#     if not len(buf):
#       break
#   # write the received data
#     sys.stdout.write(buf)
# if __name__ == '__main__':
#   main()

#

# ----------------------------------------------------------Modifying socket's send/receive buffer sizes
# import socket
# SEND_BUF_SIZE = 4096
# RECV_BUF_SIZE = 4096
# def modify_buff_size():
#   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
# # Get the size of the socket's send buffer
#   bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
#   print "Buffer size [Before]:%d" %bufsize
#   sock.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
#   sock.setsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF,SEND_BUF_SIZE)
#   sock.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,RECV_BUF_SIZE)
#   bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
#   print "Buffer size [After]:%d" %bufsize
# if __name__ == '__main__':
#   modify_buff_size()

#   output
#   Buffer size [Before]:16384
#   Buffer size [After]:8192

# ----------------------------------------------------------Changing a socket to the blocking/ non-blocking mode

# import socket
# def test_socket_modes():
#   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#   s.setblocking(0)
#   s.settimeout(0.5)
#   s.bind(("127.0.0.1", 1230))
#   socket_address = s.getsockname()
#   print "Trivial Server launched on socket: %s" %str(socket_address)
#   while(1):
#     s.listen(1)
# if __name__ == '__main__':
#   test_socket_modes()

# ----------------------------------------------------------Reusing socket addresses
#to fix Address already in use
# import socket
# import sys
# def reuse_socket_addr():
#   sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
# # Get the old state of the SO_REUSEADDR option
#   old_state = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
#   print "Old sock state: %s" %old_state
# # Enable the SO_REUSEADDR option
#   sock.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
#   new_state = sock.getsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR )
#   print "New sock state: %s" %new_state
#   local_port = 8282
#   srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#   srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#   srv.bind( ('', local_port) )
#   srv.listen(1)
#   print ("Listening on port: %s " %local_port)
#   while True:
#     try:
#       connection, addr = srv.accept()
#       print 'Connected by %s:%s' % (addr[0], addr[1])
#     except KeyboardInterrupt:
#       break
#     except socket.error, msg:
#       print '%s' % (msg,)
# if __name__ == '__main__':
#   reuse_socket_addr()

#   output
#   Old sock state: 0
#   New sock state: 1
#   Listening on port: 8282

# note:
# You may run this script from one console window and try to connect to this server from
# another console window by typing telnet localhost 8282. After you close the server
# program, you can rerun it again on the same port. However, if you comment out the line that
# sets the SO_REUSEADDR, the server will not run for the second time.


# ----------------------------------------------------------Writing a simple echo client/serverapplication
