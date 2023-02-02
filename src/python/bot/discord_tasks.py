from lightbulb.ext import tasks
import main
import time
import datetime


class taskclass():
    def __init__(self, bot, channelid, msg):
        self.bot = bot
        self.channelid = channelid
        self.msg = msg

        print("tasks initialising")

    @tasks.task(s=5)
    async def say_hi(self):
        dtime = datetime.datetime.now()
        await self.bot.rest.create_message(channel=self.channelid, content=f"hi, {dtime}")


    @tasks.task(s=0.5)
    async def send_mc_chat(self):

        if self.msg is not []:
            await self.bot.rest.create_message(channel=self.channelid, content=self.msg)
            self.msg = []
