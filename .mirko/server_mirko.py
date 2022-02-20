import socket, threading, os
from termcolor import colored

def handler(connection, addr,s):
    print("Il dispositivo ", addr,' si è collegato al server.\n')
    try:
        while True:
            data=connection.recv(10240)
            if not data:
                break
            print(data.decode("utf-8") ,'\n')
    except:
        print("Il dispositivo ",addr, 'non è più connesso al server\n')
        connection.close()

def server_starter():     
    HOST= socket.gethostbyname(socket.gethostname())
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
        os.system('cls' if os.name=='nt' else 'clear') 
        PORT= int(input("Configurazione guidata di un server\nInserire la porta di ascolto: "))
        s.bind((HOST,PORT))
        s.listen()
        os.system('cls' if os.name=='nt' else 'clear')
        print(colored("Server avviato. Mi pongo in ascolto...\n",'green'))
        while True:
            connection,addr=s.accept()
            threading.Thread(target=handler,args=(connection,addr,s,), daemon=True).start()
