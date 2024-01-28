from colorama import init, Fore
import os
import time
import importlib

class WayasMenu:
    def __init__(self):
        # colorama
        init(autoreset=True)

        self.name_user = os.getlogin()

        self.titulo_wayas = (Fore.RED +
                              """   ▄▄▌ ▐ ▄▌ ▄▄▄·  ▄· ▄▌ ▄▄▄· .▄▄ · 
    ██· █▌▐█▐█ ▀█ ▐█▪██▌▐█ ▀█ ▐█ ▀. 
    ██▪▐█▐▐▌▄█▀▀█ ▐█▌▐█▪▄█▀▀█ ▄▀▀▀█▄
    ▐█▌██▐█▌▐█ ▪▐▌ ▐█▀·.▐█ ▪▐▌▐█▄▪▐█
     ▀▀▀▀ ▀▪ ▀  ▀   ▀ •  ▀  ▀  ▀▀▀▀""" +
                              Fore.RESET)

        self.options = ("""
    1. Tools
    2. About
    3. Exit
           
           """)

        self.tools_options = ("""
    1. NGL Spammer          
    2. MyPC     
         
         """)

        self.options_yn = ("""
    1. Yes
    2. No
    """)

    def show_menu(self):
        os.system('cls')  
        print("\n" + self.titulo_wayas + "\n")
        print(self.options)
        
        option = input(f"{Fore.CYAN}{self.name_user}{Fore.RESET} >> ")
        
        if option == "1":
            self.show_tools_menu()
        elif option == "2":
            self.show_about()
        elif option == "3":
            exit()   
        else:
            print("Opción inválida")
            time.sleep(1)
            self.show_menu()

    def show_tools_menu(self):
        os.system('cls')
        print("\n" + self.titulo_wayas + "\n")
        print(self.tools_options)
        
        tool_option = input(f"{Fore.CYAN}{self.name_user}{Fore.RESET} >> ")

        if tool_option == "1":
            os.system("python tools/ngl/spammer/NGLSpamer.py")
        elif tool_option == "2":
            os.system("python tools/mypc/main.py")
        else:
            print("Opción inválida")
            time.sleep(1)
            self.show_tools_menu()

    def show_about(self):
        os.system('cls')
        credits_app = (f"""
    Coded by {Fore.CYAN}AaronWayas{Fore.RESET}                  
    With the help of: {Fore.CYAN}Codeium{Fore.RESET}
    
    Version: 1.0
    Tools Count: {Fore.RED}2{Fore.RESET}              
                  """)
        
        print("\n" + self.titulo_wayas + "\n")
        print(credits_app)
        input(f"{Fore.CYAN}{self.name_user}{Fore.RESET} >> Press enter to continue...")
        self.show_menu()

if __name__ == "__main__":
    menu = WayasMenu()
    menu.show_menu()
