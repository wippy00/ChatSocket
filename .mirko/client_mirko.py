import Init,os,socket,threading,sys,rsa,time
from termcolor import colored,cprint
from Init import Client_Values
import Settings_Menu as Settings

def msg_in(s):
    while True:
        try:
            msg=s.recv(4096)
            if not msg:
                    break
            print('\n',msg.decode('utf-8'))
        except:
            print('errore')
            break

def msg_out(s):
    while True:
        msg = input()
        msg_out_completo = Init.User.username
        msg_out_completo = msg_out_completo + ": "
        msg_out_completo = msg_out_completo + msg
        if msg_out_completo == Client_Values.host + ': :quit':
            print('[DEBUG] ":quit" detcted. Closing...') if Init.User.debug_mode == 'True' else None
            time.sleep(0.5) if Init.User.debug_mode == 'True' else None
            chiusura = "Connessione terminata dall'altro utente."                
            os.system('cls' if os.name=='nt' else 'clear')
            print(colored("Connessione terminata dall'utente. Chiusura processo...",'red'))
            s.sendall(chiusura.encode('utf-8'))
            s.close()
            sys.exit(0)
        else:
            if Init.USE_RSA == True:
                print('[DEBUG] Use_RSA is equal "True". Messages are encrypted') if Init.User.debug_mode == 'True' else None
                try:
                    Settings.Rsa_keys.rsa_generator()
                    print('[DEBUG] RSA keys created correctly') if Init.User.debug_mode == 'True' else None
                except:
                    print(colored("Errore durante la generazione delle key RSA."),'red')
                    # a = 'ciao'
                msg_out_completo_crypt = rsa.encrypt(msg_out_completo.encode(),Settings.Rsa_keys.PBkey)
                s.sendall(msg_out_completo_crypt)    
            else:
                try:
                    s.sendall(msg_out_completo.encode('utf-8'))
                except:
                    print(colored("Si è verificato un errore durante l'invio del messaggio. Controllare che il server sia disponibile", 'red'))

def connect(): #Gestisce la connessione ad un server
    if Init.USE_RSA == True:
        Settings.Rsa_keys.rsa_generator()
    try:
        Init.Config_management.config_editor.read('messaggi_settings.ini')
    except:
        print("[DEBUG] Cannot load config file. Maybe it's missing?") if Init.User.debug_mode == 'True' else None
    Init.Config_management.config_editor.sections()
    if Init.Config_management.NO_CONFIG == False:
        Client_Values.host = Init.Config_management.config_editor['NETWORK']['default_ip']
        Client_Values.port = int(Init.Config_management.config_editor['NETWORK']['default_port'])
        print('[DEBUG] Found a configfile with valid IP and port.') if Init.User.debug_mode == 'True' else None
        time.sleep(0.5) if Init.User.debug_mode == 'True' else None
    if Client_Values.host == '':
        os.system('cls' if os.name=='nt' else 'clear')
        print("Per stabilire una connessione l'utente all'altro capo deve selezionare", '"Ospita un utente" dal menu principale.')
        host = input("Inserire l'indirizzo IP dell'host a cui vuoi collegarti\n")
    if Client_Values.port == 0:
        port = int(input("Inserire la porta dell'host a cui vuoi collegarti\n"))
           
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        os.system('cls' if os.name=='nt' else 'clear')
        cprint('Comunicazione avviata.','green')
        print("Scrivere :quit o premere ^+C per scollegarsi\n")
        threading.Thread(target=msg_in,args=(s,), daemon=True).start()
        msg_out(s)
