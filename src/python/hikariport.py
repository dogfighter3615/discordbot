import socket
import threading
import time
import xml.etree.ElementTree
import hikari
import lightbulb

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip, port = "127.0.0.1", 25585
tree, guild_id, stop, connected = None, 697699096731058247, False, False
thread_minecraft = None
channelid = 822891962499596358


xmltree = xml.etree.ElementTree.parse('things.txt')
root = xmltree.getroot()
print(root)
tokens = list(root[0].attrib.values())[0] or ""
tokens = str(tokens)



bot = lightbulb.BotApp(intents=hikari.Intents.ALL, token=tokens, default_enabled_guilds=guild_id)
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

    @bot.command
    @lightbulb.command("ping","checks if the bot is alive")
    @lightbulb.implements(lightbulb.SlashCommand)
    async def ping(ctx: lightbulb.Context) ->None:
        if not ctx.author.is_bot:
            await ctx.respond("pong")
            print("pong")

    bot.run()


def main():
    discordbot()
    pass


if __name__ == "__main__":
    main()
