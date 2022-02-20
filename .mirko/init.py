import os, configparser,time
#from termcolor import colored, cprint
USE_RSA = False

class Config_management:
    if os.path.exists("messaggi_settings.ini") == 1:
        NO_CONFIG = False
    else: 
        NO_CONFIG = True
    config_editor = configparser.ConfigParser()

class User:
    username = ''
    if Config_management.NO_CONFIG == 'False':
        c = configparser.ConfigParser()
        c.read('messaggi_settings.ini')
        a = c['USER']['debug_mode']
        if a == 'True':
            debug_mode = True
        else:
            debug_mode = True

class Client_Values:
    host = ''
    port = 0

class Server_Values:
    port = 0

def conf_file_generator():
    Config_management.config_editor['NETWORK'] = {
        'default_ip': '',
        'default_port': 0,
        'encryption': True
    }
    Config_management.config_editor['USER'] = {
        'username': '',
        'debug_mode': False
    }
    Config_management.config_editor['SERVER'] = {
        'setted_up': 0,
        'default_port': 0
    }
    with open('messaggi_settings.ini', 'w') as file:
        Config_management.config_editor.write(file)
        file.close()
        input("Il file di configurazione è stato scritto nella cartella Home (User\<NomeUtente> su Windows). Premere Enter per continuare...")

def conf_file_check():
        if Config_management.NO_CONFIG == True:
            print(colored("Impossibile trovare un file di configurazione (messaggi_settings.ini).",'yellow'))
            a = input("Creare un nuovo file di configurazione? [S/n] ")
            if a =='S' or a =='s' or a =='': #Se l'utente decide di creare un file di configurazione...
                    conf_file_generator() #... crea un file di configurazione nella cartella Home (Su Windows la cartella home corrisponde a C:\Users\<nome_utente>)
                    Config_management.NO_CONFIG = False
            if a =='N' or a == 'n':
                    os.system('cls' if os.name=='nt' else 'clear')

if __name__ == '__main__':
    conf_file_check()
    from main_menu import username_input
    username_input(USE_RSA)
    