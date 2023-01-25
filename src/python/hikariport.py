import socket
import threading
import time
import xml.etree.ElementTree
import hikari
import lightbulb

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tree, stop, connected = None, False, False
thread_minecraft = None

xmltree = xml.etree.ElementTree.parse('things.txt')
root = xmltree.getroot()
print(root)

token = str(list(root[0].attrib.values())[0])
guild_id = list(root[2].attrib.values())
channelid = str(list(root[3].attrib.values())[0])
ip = str(list(root[4].attrib.values())[0])
port = int(list(root[4].attrib.values())[1])
print(ip, port, channelid)

bot = lightbulb.BotApp(intents=hikari.Intents.ALL, token=token, default_enabled_guilds=guild_id)


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
    print("connected")
    while connected and not stop:
        try:

            msg = client_socket.recv(2 ** 10)
            print("hi", msg)
            message = await bot.rest.create_message(channelid, str(msg)).send()
            print(message)
            #await sendmessage(msg)
            msg = None
        except:
            # print("failed to recieve message")
            pass


def discordbot():
    global bot
    bot.run()



def commands(bot):
    @bot.listen()
    async def ping(event: hikari.GuildMessageCreateEvent) -> None:
        print(event.message.content)
        if event.is_human and event.channel_id == channelid:
            await event.message.respond(event.message.content)

    @bot.command
    @lightbulb.command("ping", "checks if the bot is alive")
    @lightbulb.implements(lightbulb.SlashCommand)
    async def ping(ctx: lightbulb.Context) -> None:
        if not ctx.author.is_bot:
            await ctx.respond("pong")
            print("pong")

    @lightbulb.add_checks(lightbulb.owner_only)
    @bot.command()
    @lightbulb.command("stop", "close the bot")
    @lightbulb.implements(lightbulb.SlashCommand)
    async def stop(ctx: lightbulb.Context) -> None:
        global stop
        stop = True
        thread_minecraft.join()
        await ctx.respond("stopping", flags=hikari.MessageFlag.EPHEMERAL)
        await bot.close()

    @lightbulb.add_checks(lightbulb.owner_only)
    @bot.command()
    @lightbulb.command("start", "start the minecraft connection")
    @lightbulb.implements(lightbulb.SlashCommand)
    async def start(ctx: lightbulb.context) -> None:
        await ctx.respond("starting", flags=hikari.MessageFlag.EPHEMERAL)
        global thread_minecraft
        thread_minecraft.start()

    @lightbulb.add_checks(lightbulb.owner_only)
    @bot.command()
    @lightbulb.command("restart", "restarts the bot")
    @lightbulb.implements(lightbulb.SlashCommand)
    async def restart(ctx: lightbulb.SlashCommand) -> None:
        await ctx.respond("waiting for minecraft thread connection to close", flags=hikari.MessageFlag.EPHEMERAL)
        global stop
        stop = True
        thread_minecraft.join()
        await ctx.respond("restarting", flags=hikari.MessageFlag.EPHEMERAL)
        await bot.close()
        time.sleep(1)
        await main()


def main():
    global stop, thread_minecraft
    stop = False
    thread_minecraft = threading.Thread(name="thread_minecraft", target=minecraftthread)
    time.sleep(1)
    thread_discord = threading.Thread(name="thread_discord", target=discordbot)
    thread_discord.start()
    thread_discord.join()


def init():
    commands(bot)
    main()


if __name__ == "__main__":
    init()
