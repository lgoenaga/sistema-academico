import ctypes
import platform
import subprocess

def mbox():
    if platform.system() == "Windows":
        ctypes.windll.user32.MessageBoxW(0, "Aceptar", "Cancelar", 1)
    elif platform.system() == "Linux":
        result = subprocess.run(['zenity', '--question', '--text=Desea Proceder?', '--ok-label=Continuar', '--cancel-label=Cancelar'])
        if result.returncode == 0:
            return True
        else:
            return False
        
def mboxcancel():
    if platform.system() == "Windows":
        ctypes.windll.user32.MessageBoxW(0, "Aceptar", "Cancelar", 1)
    elif platform.system() == "Linux":
        subprocess.run(['zenity', '--info', '--text=Proceso Cancelado', '--ok-label=Aceptar'])
        
def mboxvacio():
    if platform.system() == "Windows":
        ctypes.windll.user32.MessageBoxW(0, "Aceptar", "Cancelar", 1)
    elif platform.system() == "Linux":
        subprocess.run(['zenity', '--info', '--text=No se ha encontrado información', '--ok-label=Aceptar'])

def mboxsuccess():
    if platform.system() == "Windows":
        ctypes.windll.user32.MessageBoxW(0, "Aceptar", "Cancelar", 1)
    elif platform.system() == "Linux":
        subprocess.run(['zenity', '--info', '--text=Proceso Exitoso', '--ok-label=Aceptar'])