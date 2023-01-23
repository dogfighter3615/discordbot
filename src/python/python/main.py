import discord
import socket
import threading
import time
import xml.etree.ElementTree

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip, port = "127.0.0.1", 25585
tree, guild_id, stop, connected = None, 697699096731058247, True, False



thread_minecraft = None
channelid = 822891962499596358


# https://trello.com/b/vSETvt7c/mc-chat-mod


class MyClient(discord.Client):
    async def on_ready(self):
        await tree.sync(guild=discord.Object(697699096731058247))
        print(f"logged on as {self.user}")

    async def on_message(self, message):
        print(message.author.name, message.content, message.channel.id)


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


def discordthread():
    global Client, token, tree
    Client.run(token)


intents = discord.Intents.all()
Client = MyClient(intents=intents)


def send_message(message: str, channelid: int) -> None:
    pass


def main():
    global tree
    tree = commands(Client)

    thread_discord = threading.Thread(name="thread_discord", target=discordthread)
    thread_discord.start()
    thread_discord.join()
    try:
        thread_minecraft.join()
    except:
        pass


def commands(Client):
    tree = discord.app_commands.CommandTree(Client)

    @tree.command(name='test', guild=discord.Object(id=guild_id))
    async def test(ctx):
        await ctx.response.send_message("Hi")
        print("Hi")

    @tree.command(name="start", guild=discord.Object(id=guild_id))
    async def start(ctx):
        global stop, thread_minecraft
        await ctx.response.send_message(content="starting", delete_after=5.0)
        stop = False
        thread_minecraft = threading.Thread(name="thread_minecraft", target=minecraftthread)
        thread_minecraft.start()
        pass

    @tree.command(name="stop", guild=discord.Object(id=guild_id))
    async def stop(ctx):
        global stop
        await ctx.response.send_message("stopping", delete_after=5.0, ephemeral=True)
        await Client.close()
        stop = True

    @tree.command(name="change_channel", guild=discord.Object(id=guild_id),
                   description="changes the channelid to send chat messages in. if empty changes to current channel")
    async def changechannel(ctx):
        pass

    return tree


if __name__ == "__main__":
    main()
