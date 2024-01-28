import os
import time
title = """   ▄▄▌ ▐ ▄▌ ▄▄▄·  ▄· ▄▌ ▄▄▄· .▄▄ · 
    ██· █▌▐█▐█ ▀█ ▐█▪██▌▐█ ▀█ ▐█ ▀. 
    ██▪▐█▐▐▌▄█▀▀█ ▐█▌▐█▪▄█▀▀█ ▄▀▀▀█▄
    ▐█▌██▐█▌▐█ ▪▐▌ ▐█▀·.▐█ ▪▐▌▐█▄▪▐█
     ▀▀▀▀ ▀▪ ▀  ▀   ▀ •  ▀  ▀  ▀▀▀▀"""

def install():
    print("\n" + title + "\n")
    print("""
    Para ejecutar el programa, debe de tener instalado
    las librerías necesarias. Escribe 1 para instalar
    lo escencial o 2 para salir.       
          
          
          
          """)
    
    option = input(">> ")
    
    if option == "1":
        os.system("pip install -r requirements.txt")
        print("Instalado!")
        time.sleep(1)
        os.system("python wayas.py")
    elif option == "2":
        exit()
    else:
        print("Invalid option")
        time.sleep(1)
        install()    
    
install()