import winreg
import os 
import getpass

def add_file_startup(name: str, file_path: str, background=True):

    file_path = file_path.replace("/", "\\")

    with winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) as hkey:
        with winreg.OpenKey(hkey, "Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_ALL_ACCESS) as sub_key:
            if background: file_path = '"{0}"{1}'.format(file_path, " --background") 
            winreg.SetValueEx(sub_key, name, 0, winreg.REG_SZ, file_path)


#exemple
add_file_startup("test", "C:/test.exe")