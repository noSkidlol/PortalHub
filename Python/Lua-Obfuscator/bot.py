from importlib.resources import path
import discord
from discord.ext import commands, tasks
import requests
import os
from os import system
import subprocess
import shutil
import keep_alive  
from itertools import cycle

token = os.environ['DISCORD_TOKEN']
channel_id = 1053895713739788368

bot = commands.Bot(command_prefix=".")
bot.remove_command("help")


def obfuscation(path, author):
  copy = f".//obfuscated//{author}.lua"

  #removing duplicates
  if os.path.exists(copy):
    os.remove(copy)

  #copying uploaded one to make operations on it
  shutil.copyfile(path, copy)

  #copying obfuscate file to copied one
  text_file = open(f".//obfuscate.lua", "r")
  data = text_file.read()
  text_file.close()
  f = open(copy, "a")
  f.truncate(0)
  f.write(data)
  f.close()

  #writing upload file into obfuscation script
  originalupload = open(path, "r")
  originalupload_data = originalupload.read()
  originalupload.close()

  with open(copy, "r") as in_file:
    buf = in_file.readlines()

  with open(copy, "w") as out_file:
    for line in buf:
      if line == "--SCRIPT\n":
        line = line + originalupload_data + '\n'
      out_file.write(line)


  output = subprocess.getoutput(f'bin/luvit {copy}')

  if os.path.exists(f".//obfuscated//{author}-obfuscated.lua"):
    os.remove(f".//obfuscated//{author}-obfuscated.lua")

  f = open(f".//obfuscated//{author}-obfuscated.lua", "a")
  f.write(output)
  f.close()

  os.remove(copy)


status = cycle([
  '.obfuscate | Working...',
  '.obfuscate | Working..',
  '.obfuscate | Working.'
])


@bot.event
async def on_ready():
  change_status.start()
  print(f"{bot.user} are now online.")
  await bot.change_presence(status=discord.Status.online,
                            activity=discord.Activity(
                              type=discord.ActivityType.watching,
                              name=next(status)))
  keep_alive.keep_alive()  

@tasks.loop(seconds=10)
async def change_status():
  await bot.change_presence(status=discord.Status.online,
                            activity=discord.Activity(
                              type=discord.ActivityType.watching,
                              name=next(status)))

@bot.event
async def on_message(message):
  channel = str(message.channel)
  author = str(message.author)
  channel = bot.get_channel(channel_id)

  try:
    url = message.attachments[0].url
    if not message.author.bot:
      #if message.channel.id == channel_id:
      if message.channel.type is discord.ChannelType.private:
        if message.attachments[0].url:
          if '.lua' not in url:
            embed = discord.Embed(title=f"Jioa Obfuscator",
                                  description=f"***You must set the file to .lua***",
                                  color=0xFF3357)
            message = await channel.send(embed=embed)
            dm = await message.author.create_dm()
            await dm.send(embed=embed)
          else:
            uploads_dir = f".//uploads//"
            obfuscated_dir = f".//obfuscated//"

            if not os.path.exists(uploads_dir):
              os.makedirs(uploads_dir)
            if not os.path.exists(obfuscated_dir):
              os.makedirs(obfuscated_dir)

            # print(f'\nNew lua script received from {author}.')
            # print(f'Attachment Link: {message.attachments[0].url}\n')
            response = requests.get(url)
            path = f".//uploads//{author}.lua"

            if os.path.exists(path):
              os.remove(path)

            open(path, "wb").write(response.content)
            obfuscation(path, author)
            embed = discord.Embed(title="Jioa Obfuscator",

description=f"• Please if you received error on the obfuscator or down. Report to SupLuaYT#5765 and say the reason",               
                                  color=0xFF3357)
            dm = await message.author.create_dm()
            await dm.send(
              embed=embed,
              file=discord.File(f".//obfuscated//{author}-obfuscated.lua"))
      if message.channel.id == channel_id:
        if message.attachments[0].url:
          if '.lua' not in url:
            embed = discord.Embed(title=f"Jioa Obfuscator",
                                  description=f"***You must set the file to .lua***",
                                  color=0xFF3357)
            message = await channel.send(embed=embed)
            dm = await message.author.create_dm()
            await dm.send(embed=embed)
          else:
            uploads_dir = f".//uploads//"
            obfuscated_dir = f".//obfuscated//"

            if not os.path.exists(uploads_dir):
              os.makedirs(uploads_dir)
            if not os.path.exists(obfuscated_dir):
              os.makedirs(obfuscated_dir)

           # print(f'\nNew lua script received from {author}.')
           # print(f'Attachment Link: {message.attachments[0].url}\n')
            response = requests.get(url)
            path = f".//uploads//{author}.lua"

            if os.path.exists(path):
              os.remove(path)

            open(path, "wb").write(response.content)
            obfuscation(path, author)
            embed = discord.Embed(title="Jioa Obfuscator",

description=f"• Please if you received error on the obfuscator or down. Report to SupLuaYT#5765 and say the reason",
                                  color=0xFF3357)
            await channel.send(
              embed=embed,
              file=discord.File(f".//obfuscated//{author}-obfuscated.lua"))
  except:
    pass


bot.run(token)
keep_alive.keep_alive()  
