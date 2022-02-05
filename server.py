import socket, threading, sys

HOST = socket.gethostbyname(socket.gethostname())
#HOST = '127.0.0.1'
PORTA = 65432
FORMAT="utf-8"
SIZE=8096

all_conn=[]
all_addr=[]
all_username=[]

def handler(my_conn,my_addr):
    
    my_usermane=my_conn.recv(SIZE)
    print('username di:',my_addr,'=',my_usermane,'\n')
    check_username(my_usermane,my_conn,my_addr)
    all_username.append(my_usermane)

    while  True:
        try:
            msg=my_conn.recv(SIZE)
        except:
            kill_conn(my_conn,my_addr,my_usermane)
            break
        if not msg:
                break
        print('inviato da: ',my_addr,'\n contenuto: ',msg,'\n')
        send_all(msg,my_conn)

def check_username(my_user,my_conn,my_addr):
    for username in all_username:
        if my_user==username:
            temp=('username gia in uso, sarai disconnesso').encode(FORMAT)
            my_conn.sendall(temp)
            all_conn.remove(my_conn)
            all_addr.remove(my_addr)
            print('utente disconnesso username duplicato:',my_user,my_addr)
            my_conn.close()
            sys.exit()

def send_all(msg,my_conn):
    for conn in all_conn:
        try:
            if conn!=my_conn:
                conn.sendall(msg)
        except:
            all_conn.remove(conn)
            conn.close()

def notify_all(my_conn,my_addr):
        for addr in all_addr:
            if  addr!=my_addr:
                temp=('utente connesso: ' + str(addr))
                my_conn.sendall(temp.encode(FORMAT))

def kill_conn(my_conn,my_addr,my_user):
    for conn in all_conn:
        if conn==my_conn:
            all_conn.remove(my_conn)
            all_addr.remove(my_addr)
            all_username.remove(my_user)
            conn.close()
            temp='utente disconnesso:' + str(my_addr)
            print(temp,'\n')
            send_all(temp.encode(FORMAT),my_conn)
            sys.exit()
    
server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST,PORTA))
server.listen()
print('\n in ascolto su: ', HOST,'\n')

while True:
    my_conn,my_addr=server.accept()
    all_conn.append(my_conn)
    all_addr.append(my_addr)
    temp=('utente connesso: ' + str(my_addr))
    print(temp,'\n')
    send_all(temp.encode(FORMAT),my_conn)
    notify_all(my_conn,my_addr)
    threading.Thread(target=handler,args=(my_conn,my_addr), daemon=True).start()
    
    Gioele_il_Giostraro='aua'