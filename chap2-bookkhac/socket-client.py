#!/usr/bin/env python3
import sys, socket, threading
from threading import Thread
import tkinter


def send(event=None):  # event is passed by binders.
    msg = my_msg_variables.get()
    my_msg_variables.set("")  # Clears input field.
    socketclient.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        socketclient.close()
        top.quit()



def on_closing(event=None):
  with lock:
    my_msg_variables.set("{quit}")
    send()

def receive():
    while True:
        try:
            msg = socketclient.recv(4096).decode("utf8")
            # parse=msg.split('+')
            # check=(parse[-1])
            # check=check.strip("[")
            # check=check.strip("]")
            # check=check.strip("'")
            # if (check ==room):
            #     strmsg=''.join(parts1[:-1])
            msg_list.insert(tkinter.END, msg)
            msg_list.see(tkinter.END)
        except OSError:
            break


# define variables
# print("nhap host:")
# HOST=input()
HOST="127.0.0.1"
PORT=30001
ADDR=(HOST,PORT)
lock=threading.Lock()

socketclient=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketclient.connect(ADDR)

top = tkinter.Tk()
top.title("Chat On!")

messages_frame = tkinter.Frame(top)
my_msg_variables = tkinter.StringVar()  # For the messages to be sent.
my_msg_variables.set("")
scrollbar = tkinter.Scrollbar(messages_frame)  # To see through previous messages.
# this will contain the messages.
msg_list = tkinter.Listbox(messages_frame, height=30, width=100, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg_variables)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=send)
send_button.pack()


if __name__ == '__main__':
  top.protocol("WM_DELETE_WINDOW", on_closing)
  receive_thread = Thread(target=receive)
  receive_thread.start()
  tkinter.mainloop()  # for start of GUI  Interface


