from lightbulb.ext import tasks
import main
import time
import datetime

class taskclass():
    def __init__(self, bot, channelid):
        self.bot = bot
        self.channelid = channelid
        print("tasks initialising")

    @tasks.task(s=5)
    async def say_hi(self):
        dtime = datetime.datetime.now()
        await self.bot.rest.create_message(channel=channelid, content=f"hi, {dtime}")
        time.sleep(5)

    @tasks.task(s=0.5)
    async def send_mc_chat(self):
        global msg
        msg = main.minecraft_recieve_message()
        if not msg is []:
            msg = main.minecraft_message_handler(msg)
            await self.bot.rest.create_message(channel=channelid, content=msg)
            msg = []