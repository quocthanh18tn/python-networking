Multiplexing Socket I/O for Better Performance
==============================================
purpose:
we will be using two or few clients, readers are free to extend
the recipes of this chapter and use them with tens and hundreds of clients.

1/Using ForkingMixIn in your socket server applications
introduce:You have decided to write an asynchronous Python socket server application. The server will
not block in processing a client request. So the server needs a mechanism to deal with each
client independently.

forknetwork.py will implement
see document to understand full code
todo learn OOP to understand inherit

2/Using ThreadingMixIn in your socket server applications

its quite easy to understand than fork framwork

