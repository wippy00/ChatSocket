import socket, threading, re


#HOST = '192.168.0.11'
HOST = '192.168.1.111'

PORTA = 65432
FORMAT="utf-8"
SIZE=8096

def msg_send(client):
    while True:
        msg=input()
        msg=USERNAME+msg
        client.send(msg.encode(FORMAT))

def msg_recive(client):
    while True:
        try:
            msg=client.recv(SIZE)
            if not msg:
                    break
            print(msg.decode(FORMAT))
        except:
            print('errore')
            break

USERNAME = input('inserisci username: ')
USERNAME=USERNAME+': '
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST,PORTA))
client.sendall(USERNAME.encode(FORMAT))
aua=str(client)
result = re.search("laddr=(.*)',", aua).group(1)[2:20]
print('dati connessione: ' + str(result) + '\n')
threading.Thread(target=msg_recive,args=(client,), daemon=True).start()
msg_send(client)
