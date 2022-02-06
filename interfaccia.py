import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import Scrollbar
import client

# def poke(msg):
#     messagebox.showinfo("You Have Been Poked", msg)
#     return

# def upload():
#     root.fileframe = filedialog.askopenfilename(initialdir="/", title="Seleziona un file")
#     return

def msg_append(msg):
    text_chat_log.config(state=tk.NORMAL)
    text_chat_log.insert(tk.END, msg+"\n\n")
    text_chat_log.config(state=tk.DISABLED)
    text_chat_log.see(tk.END)
    return

def msg_send():
    msg=entry_msg_write.get()
    msg=client.USERNAME+msg
    msg_append(msg)
    return

root = tk.Tk()
root.title("aua")
# root.iconbitmap("./icon.ico")
root.geometry("660x420")
#root.resizable(False, False)

##############################################################################################
#   FRAME   CONTENITORE
frame_msg_display = tk.Frame(root, width=30, height=20)
frame_msg_display.pack()
frame_msg_display.pack_propagate(0)
#   TEXT FRAME MESSAGGI
text_chat_log = tk.Text(frame_msg_display, bg="white")
text_chat_log.grid(row=0,column=0, sticky='ew')
text_chat_log.config(state=tk.DISABLED)
#   SCROLLBAR
scrollbar = tk.Scrollbar(frame_msg_display, orient='vertical', command=text_chat_log.yview)
scrollbar.grid(row=0, column=1, sticky='ns')
text_chat_log['yscrollcommand'] = scrollbar.set

##############################################################################################
#   FRAME   CONTENITORE
frame_msg_send = tk.Frame(root)
frame_msg_send.pack(pady=2)
#   ENTRY MESSAGGI
entry_msg_write = tk.Entry(frame_msg_send, width=95)
entry_msg_write.grid(row=0, column=0, columnspan=3)
#   BOTTONE SEND
button_msg_send = tk.Button(frame_msg_send, width=10, text="invia", command=msg_send)
button_msg_send.grid(row=0, column=4)





root.mainloop()