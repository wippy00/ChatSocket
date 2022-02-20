import os,time,sys
import init as Init,client as Client,server as Server, settings
import settings_menu as Settings
USER = init.User.username

def username_input(USE_RSA):
    USER = str(input("Inserire uno username: \n"))
    Init.Config_management.config_editor.read('messaggi_settings.ini')
    Init.Config_management.config_editor.sections()
    if Init.Config_management.NO_CONFIG == False:
        if bool(Init.Config_management.config_editor['NETWORK']['encryption']) == False:
              USE_RSA == False
    main_menu()


def main_menu():
    while True:
        os.system('cls' if os.name=='nt' else 'clear')
        current_time = time.strftime("%H", time.localtime())
        if int(current_time) >= 6 and int(current_time) <= 12:
            greet = "Buongiorno, "
        elif int(current_time) > 12 and int(current_time) < 18:
            greet = "Buon pomeriggio,"
        else:
            greet = "Buona sera,"
        print(greet, USER, "\nSelezionare un'opzione [C]: \n[Q] Esci\n[C] Connettiti\n[H] Ospita una chat (WIP)\n[S] Impostazioni")
        switcher(input())

def close(): #Chiude il programma. Equivalente a ":quit" durante la chat
    sys.exit(0)

def switcher(value): #Rende la selezione più semplice
    if value == 'c' or value == 'C' or value == '': #Pressione di C
        Client.connect()
    elif value == 'q' or value =='Q': #Pressione di Q
        os.system('cls' if os.name=='nt' else 'clear')
        close()
    elif value == 'h' or value =='H': #Pressione di H
        Server.server_starter()
    elif value == 's' or value == 'S': #Pressione di S
        if Init.Config_management.NO_CONFIG == True:
           Settings.settings_conf_req() 
        else:
            Settings.settings()
    elif value == 's1' or value == 'S1':
        if Init.Config_management.NO_CONFIG == True:
           Settings.settings_conf_req() 
        else:
            Settings.client()
    elif value == 's2' or value == 'S2':
        if Init.Config_management.NO_CONFIG == True:
           Settings.settings_conf_req() 
        else:
            Settings.server()