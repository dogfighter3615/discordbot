import socket
import threading
import time
from lightbulb.ext import tasks
import datetime
import commands
from global_vars import * #tree, task, ip, port, root, xmltree, channelid, bot, stop, msg, connected, guild_id, \
    #client_socket


#class taskclass():
#    def __init__(self):
#        print("tasks initialising")
#
#    @tasks.task(s=5)
#    async def say_hi(self):
#        dtime = datetime.datetime.now()
#        await bot.rest.create_message(channel=channelid, content=f"hi, {dtime}")
#        time.sleep(5)
#
#    @tasks.task(s=0.5)
#    async def send_mc_chat(self):
#        global msg
#        msg = minecraft_recieve_message()
#        if not msg is []:
#            msg = minecraft_message_handler(msg)
#            await bot.rest.create_message(channel=channelid, content=msg)
#            msg = []


async def minecraft_connect():
    client_socket.settimeout(3)
    while not connected and not stop:
        print(threading.current_thread(), threading.activeCount(), threading.enumerate())
        try:
            print("attempting connection!")
            client_socket.connect((ip, port))
            connected = True
        except:
            print("connection failed, trying again in 3 seconds")
            time.sleep(3)
    print("connected")


def minecraft_recieve_message():
    global msg
    try:
        msg = client_socket.recv(2 ** 10)
        print("hi", msg)
        return msg.decode("UTF-8")
    except:
        # print("failed to recieve message")
        pass


def minecraft_message_handler(msg: str) -> str:
    if msg.startswith("p"):
        msg = msg[1:]
        return msg
    else:
        return None


def discordbot():
    global bot
    bot.run()


def main():
    global stop
    stop = False
    time.sleep(1)
    thread_discord = threading.Thread(name="thread_discord", target=discordbot)
    thread_discord.start()
    thread_discord.join()


def init():
    commands.initcommands()
    main()


if __name__ == "__main__":
    init()
