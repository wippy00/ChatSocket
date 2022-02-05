import os,configparser,time,rsa,Init
from termcolor import colored 
class Rsa_keys:
    def rsa_generator():
        Rsa_keys.PBkey, Rsa_keys.PVkey = rsa.newkeys(256)

def sub1_settings(a):
    os.system('cls' if os.name=='nt' else 'clear')
    if a == '1':
        client()
    if a == '2':
        server()
    return 0

def settings():
    os.system('cls' if os.name=='nt' else 'clear')
    print("Impostazioni","\nSelezionare un'opzione: \n[Q] Torna al menu principale\n[1] Opzioni Client\n[2] Opzioni Server")
    a = input()
    sub1_settings(a)
    return 0

def switcher_client(value): 
    if value == 'q' or value == 'Q':
        return 0
    if value == '1':
        config_editor = configparser.ConfigParser()
        os.system('cls' if os.name=='nt' else 'clear')
        config_editor.read('messaggi_settings.ini')
        config_editor.set('NETWORK', 'default_ip', str(input("Inserire il nuovo IP di default:\n")))
        try:
            with open('messaggi_settings.ini', 'w') as file:
                config_editor.write(file)
            print(colored('Impostazioni modificate correttamente.','green'))
        except:
            print(colored('Errore durante la scrittura della key nel file di configurazione.','red'))
            print(colored("Controllare o ricreare il file di configurazione e riprovare.",'red'))
        time.sleep(1)
        return 0
    if value == '2':
        config_editor = configparser.ConfigParser()
        os.system('cls' if os.name=='nt' else 'clear')
        config_editor.read('messaggi_settings.ini')
        config_editor.set('NETWORK', 'default_port', str(input("Inserire il nuovo IP di default:\n")))
        try:
            with open('messaggi_settings.ini', 'w') as file:
                config_editor.write(file)
            print(colored('Impostazioni modificate correttamente.','green'))
        except:
            print(colored('Errore durante la scrittura della key nel file di configurazione.','red'))
            print(colored("Controllare o ricreare il file di configurazione e riprovare.",'red'))
        time.sleep(1)
        return 0
    if value == '3':
        config_editor = configparser.ConfigParser()
        os.system('cls' if os.name=='nt' else 'clear')
        config_editor.read('messaggi_settings.ini')
        a = config_editor['USER']['debug_mode']
        if a == 'True':
            a = 'False'
        else:
            a = 'True'
        config_editor.set('USER', 'debug_mode', a)
        try:
            with open('messaggi_settings.ini', 'w') as file:
                config_editor.write(file)
            print(colored('Impostazioni modificate correttamente.','green'))
        except:
            print(colored('Errore durante la scrittura della key nel file di configurazione.','red'))
            print(colored("Controllare o ricreare il file di configurazione e riprovare.",'red'))
        time.sleep(1)
        return 0

def client():
    os.system('cls' if os.name=='nt' else 'clear')
    print("Editor degli indirizzi di default","\nSelezionare un'opzione: \n[Q] Torna al menu principale\n[1] IP di default\n[2] Porta di default")
    from Init import Config_management as c
    if c.NO_CONFIG == False:      
        config_editor = configparser.ConfigParser()
        config_editor.read('messaggi_settings.ini')
        config_editor.sections()
        if config_editor['USER']['debug_mode'] == 'True':
            print('[3] Disattiva modalità Debug')
            print('[DEBUG] Found "debug_mode: True" in config file') if Init.User.debug_mode == 'True' else None
        elif config_editor['USER']['debug_mode'] == 'False':
            print('[3] Attiva modalità Debug')
            print('[DEBUG] Found "debug_mode: False" in config file') if Init.User.debug_mode == 'True' else None  
        else:    
            print(colored("Errore durante la lettura della chiave [USER][debug_mode]. Il file di configurazione potrebbe essere corrotto.",'red'))
            print(colored("Controllare o ricreare il file di configurazione e riprovare.",'red'))
        switcher_client(input())
        return 0

def switcher_server(value): #Rende la selezione più semplice
    if value == 'q' or value == 'Q':
        return 0
    if value == '1':
        config_editor = configparser.ConfigParser()
        config_editor.read('messaggi_settings.ini')
        config_editor.set('SERVER', 'default_ip', str(input("Inserire la nuova porta di default:\n")))
        try:
            with open('messaggi_settings.ini', 'w') as file:
                config_editor.write(file)
                print(colored('Impostazioni modificate correttamente.','green'))
        except:
                print(colored('Errore durante la scrittura della key nel file di configurazione.','red'))
                print(colored("Controllare o ricreare il file di configurazione e riprovare.",'red'))
        time.sleep(1)
        return 0

    
def server():
    os.system('cls' if os.name=='nt' else 'clear')
    print("Configuratore server","\nSelezionare un'opzione: \n[Q] Torna al menu principale\n[1] Porta di default (Server)")
    switcher_server(input())
    return 0

