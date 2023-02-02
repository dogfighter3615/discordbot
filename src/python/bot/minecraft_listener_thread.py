from global_vars import *
from src.python.bot import packethandler, global_vars


def listen():
    client_socket.settimeout(3)
    while connected and not stop:
        pass
        received = client_socket.recv(2**10)
        if received is not None:
            global_vars.msg = packethandler.unpack(received)
        received = None
