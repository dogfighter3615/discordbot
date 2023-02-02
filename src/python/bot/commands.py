import threading
import time
from global_vars import *
from src.python.bot import global_vars, minecraft_listener_thread


def initcommands():
    @bot.listen()
    async def ping(event: hikari.GuildMessageCreateEvent) -> None:
        print(event.message.content)
        print(channelid, event.channel_id, event.author, event.member)
        # if event.is_human and event.channel_id == channelid:
        #    await event.message.respond(event.message.content)

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
    async def stop_bot(ctx: lightbulb.Context) -> None:
        stop = True
        await ctx.respond("stopping", flags=hikari.MessageFlag.EPHEMERAL)
        await bot.close()

    @lightbulb.add_checks(lightbulb.owner_only)
    @bot.command()
    @lightbulb.command("start", "start the minecraft connection")
    @lightbulb.implements(lightbulb.SlashCommand)
    async def start(ctx: lightbulb.context) -> None:
        await ctx.respond("starting", flags=hikari.MessageFlag.EPHEMERAL)
        await main.minecraft_connect()
        minecraft_thread = threading.Thread(name="minecraft_thread", target=minecraft_listener_thread.receive)
        minecraft_thread.start()
        main.task.send_mc_chat.start()

    @lightbulb.add_checks(lightbulb.owner_only)
    @bot.command()
    @lightbulb.command("restart", "restarts the bot")
    @lightbulb.implements(lightbulb.SlashCommand)
    async def restart(ctx: lightbulb.SlashCommand) -> None:
        try:
            await ctx.respond("waiting for minecraft thread connection to close", flags=hikari.MessageFlag.EPHEMERAL)
            global_vars.stop = True
        except:
            pass
        await ctx.respond("restarting", flags=hikari.MessageFlag.EPHEMERAL)
        await bot.close()
        time.sleep(1)
        await main.main()

    @lightbulb.add_checks(lightbulb.owner_only)
    @lightbulb.option("channelid", "channel id to change to")
    @bot.command()
    @lightbulb.command("changechannel", "change the channel in which messages are send")
    @lightbulb.implements(lightbulb.SlashCommand)
    async def change_channel(ctx: lightbulb.Context):
        await ctx.respond(f"changed channel to {ctx.options.channelid}")
        channelid = int(ctx.options.channelid)
        root[3].set("channel_id", str(channelid))
        xmltree.write("things.xml")

    @bot.command()
    @lightbulb.command(name="sayhi", description="say hi a lot of times")
    @lightbulb.implements(lightbulb.SlashCommand)
    async def sayhi(ctx: lightbulb.Context):
        await ctx.respond(f"hi, {channelid}")
        task.say_hi.start()

    @bot.command()
    @lightbulb.command(name="stopsayhi", description="say hi a lot of times")
    @lightbulb.implements(lightbulb.SlashCommand)
    async def stopsayhi(ctx: lightbulb.Context):
        await ctx.respond("hi")
        task.say_hi.stop()
