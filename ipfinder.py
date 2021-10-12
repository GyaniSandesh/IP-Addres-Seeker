#At most of the case,you will have socket pre-installed in your device but if you don't have socket installed then install it by writing the command   "pip install python-socketio"
import socket
hn = socket.gethostname()
ip = socket.gethostbyname(hn)
print(f"Your ip address is {ip}")