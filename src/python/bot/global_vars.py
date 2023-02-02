import socket
import xml.etree.ElementTree
import lightbulb
from lightbulb.ext import tasks
import hikari
import main
import discord_tasks

# reading the things.txt xml file
xmltree = xml.etree.ElementTree.parse('C:/Users/david/PycharmProjects/discordbot/src/python/bot/things.xml')
root = xmltree.getroot()
print(root)

token = str(list(root[0].attrib.values())[0])
guilds = list(root[2].attrib.values())
channelid = str(list(root[3].attrib.values())[0])
ip = str(list(root[4].attrib.values())[0])
port = int(list(root[4].attrib.values())[1])

# processing the guild ids
guild_id = []
for x in guilds:
    guild_id.append(int(x))

print(ip, port, channelid)

# setting up some rest variables
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bot = lightbulb.BotApp(intents=hikari.Intents.ALL, token=token, default_enabled_guilds=guild_id)
tasks.load(bot)
msg, chatmsg = [], []
task = discord_tasks.taskclass(bot, channelid, msg)
stop = True
connected = False
