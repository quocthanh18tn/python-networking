#!/usr/bin/env python3
import sys, socket, threading
import tincanchat
import argparse
import tkinter

## ham khoi tao moi khi co 1 client vao
## y tuong se send ten va so phong de dinh dang va hien thi
def setup(event=None):
  entry_field_name.config(state=tkinter.DISABLED)
  entry_field_room.config(state=tkinter.DISABLED)
  send_button_setup.config(state=tkinter.DISABLED)
  send_button.config(state=tkinter.NORMAL)
  name_msg=name.get()
  tincanchat.send_msg(sock,name_msg)
  room_msg=room.get()
  tincanchat.send_msg(sock,room_msg)
  msg_when_connect_room="WELCOME {} JOIN ROOM NUMBER {}".format(name_msg,room_msg)
  msg_list.insert(tkinter.END,msg_when_connect_room)
  msg_when_quit="TYPE MESSAGES, ENTER OR CLICK TO SEND. 'q' TO QUIT"

  msg_list.insert(tkinter.END,msg_when_quit)
  msg_when_other_connect="init{} has connected".format(name_msg)
  my_msg.set(msg_when_other_connect)
  send()
  # msg_list.insert(tkinter.END,msg_when_quit)
  # Create thread for handling user input and message sending
  thread = threading.Thread(target=handle_input,args=[sock,name_msg,room_msg],daemon=True)
  thread.start()

def send(event=None):  # event is passed by binders.
    msg = str(my_msg.get())
    print(msg)
    my_msg.set("")  # Clears input field.
    tincanchat.send_msg(sock,msg)
    if msg == "q":
        sock.close()
        top.quit()


def handle_input(sock,name,room):
    rest = bytes()
    while True:
            (msgs, rest) = tincanchat.recv_msgs(sock, rest)
            for msg in msgs:
                parts1 = msg.split('+')
                splitpart1=parts1[0].split(':')
                name_clearly=splitpart1[0].strip("[")
                name_clearly=name_clearly.strip("]")
                name_clearly=name_clearly.strip("'")
                init=splitpart1[1][1:5]
                var_thongbaoconnect=splitpart1[1][5:]
                print(var_thongbaoconnect)
                check=(parts1[-1])
                check=check.strip("[")
                check=check.strip("]")
                check=check.strip("'")
                if (check ==room):
                    if(init=="init"):
                        msg_list.insert(tkinter.END,var_thongbaoconnect)
                    else:
                        if(splitpart1[1]==' q'):
                            mes_exit="{} has exited".format(name_clearly)
                            msg_list.insert(tkinter.END,mes_exit)
                        else:
                            mes_full="{}:{}".format(name_clearly,splitpart1[1])
                            msg_list.insert(tkinter.END,mes_full)

# def on_closing(event=None):
#     my_msg.set("q")
#     send()

HOST = sys.argv[-1] if len(sys.argv) > 1 else '127.0.0.1'
PORT = tincanchat.PORT

top = tkinter.Tk()
top.title("Chat On!")
messages_frame = tkinter.Frame(top)

my_msg  = tkinter.StringVar()  # For the messages to be sent.
name    = tkinter.StringVar()  # For the messages to be sent.
room    = tkinter.StringVar()  # For the messages to be sent.
my_msg.set("")
name.set("")
room.set("")

tkinter.Label(top, text="Name",bg="black", width=15, fg="white").pack(ipady=10,side="top")
entry_field_name = tkinter.Entry(top, textvariable=name)
entry_field_name.pack(side="top",ipady=5)

tkinter.Label(top, text="Room number", width=15,bg="black", fg="white").pack(side="top",ipady=10)
entry_field_room = tkinter.Entry(top, textvariable=room)
entry_field_room.pack(side="top",ipady=5)
send_button_setup = tkinter.Button(top, width=10,height=2, text="Setup", command=setup)
send_button_setup.pack()

scrollbar = tkinter.Scrollbar(messages_frame)  # To see through previous messages.
msg_list = tkinter.Listbox(messages_frame, height=25, width=100, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top,text="Send",height=2, command=send,state=tkinter.DISABLED)
send_button.pack()

# top.protocol("WM_DELETE_WINDOW", on_closing)


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
msg='Please type your name and your room number above to start chat app'
msg_list.insert(tkinter.END,msg)

tkinter.mainloop()  # for start of GUI  Interface
