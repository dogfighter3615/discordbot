import socket
import threading
import time
import commands
from src.python.bot import global_vars
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
    global_vars.client_socket.settimeout(3)
    failure = 0
    while not global_vars.connected and not global_vars.stop and not failure >= 10:
        print(threading.current_thread(), threading.activeCount(), threading.enumerate())
        try:
            print("attempting connection!")
            client_socket.connect((ip, port))
            global_vars.connected = True
        except:
            print(f"connection failed, trying again in 3 seconds, {10-failure} tries left")
            failure += 1
            time.sleep(3)

    if global_vars.connected:
        print("connected")

    elif failure >= 10:
        print("failed to connect try again")


def minecraft_recieve_message():
    global msg
    try:
        msg = client_socket.recv(2 ** 10)
        print("hi", msg)
        return msg.decode("UTF-8")
    except:
        # print("failed to recieve message")
        pass


def discordbot():
    bot.run()


def main():
    global_vars.stop = False
    time.sleep(1)
    thread_discord = threading.Thread(name="thread_discord", target=discordbot)
    thread_discord.start()
    thread_discord.join()


def init():
    commands.initcommands()
    main()


if __name__ == "__main__":
    init()
