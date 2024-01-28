import socket
import platform
import psutil
import cpuinfo
from colorama import Fore
import os

title = (Fore.RED) + """
    • ▌ ▄ ·.  ▄· ▄▌     ▄▄▄· ▄▄· 
    ·██ ▐███▪▐█▪██▌    ▐█ ▄█▐█ ▌▪
    ▐█ ▌▐▌▐█·▐█▌▐█▪     ██▀·██ ▄▄
    ██ ██▌▐█▌ ▐█▀·.    ▐█▪·•▐███▌
    ▀▀  █▪▀▀▀  ▀ •     .▀   ·▀▀▀ 
                            by wayas

""" + (Fore.RESET)

def get_computer_name():
    return socket.gethostname()

def get_ip_address():
    return socket.gethostbyname(socket.gethostname())

def get_cpu_info():
    info = cpuinfo.get_cpu_info()
    return info['brand_raw']

def get_ram_info():
    ram = psutil.virtual_memory()
    return f"Total: {ram.total >> 30:.2f} GB, Disponible: {ram.available >> 30:.2f} GB"

def get_os_info():
    return f"Sistema Operativo: {platform.system()} {platform.version()}"

def main():
    os.system('cls')
    print(title)
    print(f"Nombre del ordenador: {get_computer_name()}")
    print(f"Dirección IP: {get_ip_address()}")
    print(f"CPU: {get_cpu_info()}")
    print(f"RAM: {get_ram_info()}")
    print(get_os_info())
    input("\n" + "Preciona Enter para ir a Wayas" + "\n")
    
    os.system("python C:/Users/aaron/OneDrive/Escritorio/Aaron/1/wayas.py")

if __name__ == "__main__":
    main()
