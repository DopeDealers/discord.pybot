import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import platform
import sys
import os
import random
import requests
import urllib.request
import json
import time
import config


client = Bot(description=config.descr, command_prefix=config.prefix)




@client.event
async def on_ready():
     print("Online!")
     print("Currently active on " + str(len(client.servers)) + " servers.")
     await client.change_presence(game=discord.Game(name="on testing"))


@client.command(pass_context=True, aliases=['remove', 'delete'])
async def purge(ctx, number):
    try:
        if ctx.message.author.server_permissions.administrator:
            mgs = []
            number = int(number)
            async for x in client.logs_from(ctx.message.channel, limit=number):
                mgs.append(x)
            await client.delete_messages(mgs)
            print("Purged {} messages.".format(number))
            logger.info("Purged {} messages.".format(number))
        else:
            await client.say(config.err_msg_perm)
    except:
           await client.say("Purged {} messages.".format(number))

@client.command(pass_context=True)
async def ping(ctx):
    try:
        pingtime = time.time()
        pingms = await client.say("*Pinging...*")
        ping = (time.time() - pingtime) * 1000
        await client.edit_message(pingms, "**Pong!** :ping_pong:  The ping time is `%dms`" % ping)
        print("Pinged bot with a response time of %dms." % ping)
        logger.info("Pinged bot with a response time of %dms." % ping)


client.run(config.token)