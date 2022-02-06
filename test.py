import tkinter as tk
from tkinter import LEFT, RIGHT, TOP, messagebox
from tkinter import filedialog
from tkinter.ttk import Scrollbar

username="mario: "

def poke(msg):
    messagebox.showinfo("You Have Been Poked", msg)
    return

def upload():
    root.fileframe = filedialog.askopenfilename(initialdir="/", title="Seleziona un file")
    return

def msg_append(msg):
    text_chat_log.config(state=tk.NORMAL)
    text_chat_log.insert(tk.END, msg+"\n\n")
    text_chat_log.config(state=tk.DISABLED)
    text_chat_log.see(tk.END)
    return

def msg_send():
    msg=entry_msg_write.get()
    msg=username+msg
    msg_append(msg)
    return


root = tk.Tk()
root.title("aua")
# root.iconbitmap("./icon.ico")
root.geometry("600x600")
#root.resizable(False, False)

text_chat_log = tk.Text(root, bg="white")
text_chat_log.pack(side=RIGHT)
text_chat_log.config(state=tk.DISABLED)

scrollbar = tk.Scrollbar(root, orient='vertical', command=text_chat_log.yview)
scrollbar.pack(side=LEFT)
text_chat_log['yscrollcommand'] = scrollbar.set


entry_msg_write = tk.Entry(root, width=85)
entry_msg_write.pack(side=RIGHT)

button_msg_send = tk.Button(root, width=10, text="invia", command=msg_send)
button_msg_send.pack(side=LEFT)







root.mainloop()