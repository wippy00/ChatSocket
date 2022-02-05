import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog



def send():
    mylabel = tk.Label(root, text=msg_E.get())
    mylabel.grid(row=9, column=0)

def poke():
    messagebox.showinfo("aua", "hey wake up")

def upload():
    root.fileframe = filedialog.askopenfilename(initialdir="/", title="Seleziona un file")

def msg_display(usr,msg):
    msg_label= tk.LabelFrame(root, text=msg, padx=5, pady=5)
    



root= tk.Tk()
root.title("aua")
#root.iconbitmap("./icon.ico")
root.geometry("600x600")
root.resizable(False, False)

frame_msg = tk.Frame(root, width= 600, height=500,bg="blue")
frame_send = tk.Frame(root, width= 6000, height=100,bg="blue")

label_msg= tk.LabelFrame(frame_msg, text="aua", padx=5, pady=5)

msg_E = tk.Entry(frame_send, width=80)
send_B = tk.Button(frame_send, width=10, text="aua", command=poke)



frame_msg.grid(row=0,column=0)
frame_send.grid(row=1, column=0)
send_B.grid(row=0, column=4, padx=5, pady=5)
msg_E.grid(row=0, column=0, columnspan=3, padx=5, pady=5)
label_msg.pack()
send()

root.mainloop()