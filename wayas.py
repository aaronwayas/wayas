from colorama import init, Fore
import os
import time

nameUSer = os.getlogin()

# colorama
init(autoreset=True)

titulo_wayas = (Fore.RED +
              """   ▄▄▌ ▐ ▄▌ ▄▄▄·  ▄· ▄▌ ▄▄▄· .▄▄ · 
    ██· █▌▐█▐█ ▀█ ▐█▪██▌▐█ ▀█ ▐█ ▀. 
    ██▪▐█▐▐▌▄█▀▀█ ▐█▌▐█▪▄█▀▀█ ▄▀▀▀█▄
    ▐█▌██▐█▌▐█ ▪▐▌ ▐█▀·.▐█ ▪▐▌▐█▄▪▐█
     ▀▀▀▀ ▀▪ ▀  ▀   ▀ •  ▀  ▀  ▀▀▀▀""" +
              Fore.RESET)

options = ("""
    1. Tools
    2. About
    3. Exit
           
           """    ) 

toolsWayas = ("""
    1. NGL Spammer          
    2. MyPC     
         
         """)

def menuWayas():
    os.system('cls')  
    print("\n" + titulo_wayas + "\n")
    print(options)
    
    option = input(f"{Fore.CYAN}{nameUSer}{Fore.RESET} >> ")
    
    if option == "1":
        tools()
    elif option == "2":
        about()
    elif option == "3":
        exit()   
    else:
        print("Invalid option")
        time.sleep(1)
        menuWayas()
        
 
def tools():    
    os.system('cls')
    print("\n" + titulo_wayas + "\n")
    print(toolsWayas)
    option = input(f"{Fore.CYAN}{nameUSer}{Fore.RESET} >> ")
    
    # All tools
    # Tools
    if option == "1":
        os.system("python tools/ngl/spammer/NGLSpamer.py")

    elif option == "2":
        os.system("python tools/mypc/main.py")
    
    
    # Tools
    # Tools
def about():
    os.system('cls')
    creditsApp = (f"""
    Coded by {Fore.CYAN}AaronWayas{Fore.RESET}                  
    With the help of: {Fore.CYAN}Codeium{Fore.RESET}
    
    Version: 1.0
    Tools Count: {Fore.RED}2{Fore.RESET}              
                  """)
    
    print("\n" + titulo_wayas + "\n")
    print(creditsApp)
    input(f"{Fore.CYAN}{nameUSer}{Fore.RESET} >> Press enter to continue...")
    menuWayas()

if __name__ == "__main__":
    menuWayas()
