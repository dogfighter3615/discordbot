import hikari
import socket
import threading
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip, port = "127.0.0.1", 25585
tree, guild_id, stop, connected = None, 697699096731058247, False, False
token = 'MTAzNjc0Mjc1OTI5OTY4NjUxMg.GsNOk7.EwVggeH0YfF6EQAm4hmrmx1DdWj_oP12rgK0uU'
thread_minecraft = None
channelid = 822891962499596358
bot = hikari.GatewayBot(intents=hikari.Intents.ALL, token=token)


# https://trello.com/b/vSETvt7c/mc-chat-mod


def minecraftthread():
    global client_socket, stop, connected
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
    while connected and not stop:
        try:
            print("connected")
            msg = client_socket.recv(2 ** 10)
            print("hi", msg)
            msg = None
        except:
            # print("failed to recieve message")
            pass


def discordbot():
    global bot, channelid

    @bot.listen()
    async def ping(event: hikari.GuildMessageCreateEvent) -> None:
        if event.is_human and event.channel_id == channelid:
            await event.message.respond(event.message.content)

    bot.run()


def main():
    discordbot()
    pass


if __name__ == "__main__":
    main()
