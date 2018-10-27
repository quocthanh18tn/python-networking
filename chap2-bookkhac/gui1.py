from tkinter import *
import tkinter
def send():
  e1.config(state=DISABLED)
  e2.config(state=DISABLED)
  but.config(state=DISABLED)
  msg_list.insert(tkinter.END,name.get())
  msg_list.insert(tkinter.END,room.get())

top = tkinter.Tk()
top.title("Chat On!")
Label(top, text="Name").pack()
Label(top, text="Room number").pack()
name = tkinter.StringVar()  # For the messages to be sent.
room = tkinter.StringVar()  # For the messages to be sent.

e1 = tkinter.Entry(top,textvariable=name)
e2 = tkinter.Entry(top,textvariable=room)

e1.pack()
e2.pack()
but = tkinter.Button(top,
                   text="Comfirm",
                   fg="red",
                   command=send)
but.pack()



messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()  # For the messages to be sent.
my_msg.set("")
scrollbar = tkinter.Scrollbar(messages_frame)  # To see through previous messages.
# this will contain the messages.
msg_list = tkinter.Listbox(messages_frame, height=30, width=100, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=send)
send_button.pack()

top.protocol("WM_DELETE_WINDOW", send)


mainloop( )