import socket
import xml
import lightbulb
import hikari
import main
import discord_tasks

xmltree = xml.etree.ElementTree.parse('things.txt')
root = xmltree.getroot()
print(root)

token = str(list(root[0].attrib.values())[0])
guilds = list(root[2].attrib.values())
channelid = str(list(root[3].attrib.values())[0])
ip = str(list(root[4].attrib.values())[0])
port = int(list(root[4].attrib.values())[1])

guild_id = []
for x in guilds:
    guild_id.append(int(x))

print(ip, port, channelid)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

bot = lightbulb.BotApp(intents=hikari.Intents.ALL, token=token, default_enabled_guilds=guild_id)
main.tasks.load(bot)

task = discord_tasks.taskclass(bot, channelid)
