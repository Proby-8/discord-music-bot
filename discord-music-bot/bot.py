from random import randint
import discord
from discord.ext import commands

# get token for bot
file1 = open("discord-music-bot\\lib\\secret.txt", 'r')
TOKEN = file1.readline()
file1.close() 

# set up bot
client = commands.Bot(command_prefix="!", help_command=None, intents=discord.Intents.all())

#on start up
@client.event
async def on_ready():  # runs when the bot goes online
    print('Logged in as')
    print(client.user.name)
    print('------')

    await client.change_presence(status=discord.Status.do_not_disturb)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="top tier music"))

# help menu
@client.command()
async def help(ctx):
    await ctx.send("```yaml\n"
                   "!join\nConnects the bot to your voice channel\n\n"
                   "!av <target>\nDisplays full-size profile picture of target\n\n"
                   "```")
    
# works
# allow the bot to be invited to servers
@client.command()
async def invite(ctx):
    await ctx.send("Click this link to invite me to your server!\n"
                   "https://discord.com/api/oauth2/authorize?client_id=812037295040364584&permissions=8&scope=bot")
    
# works
# change nickname of a user
@client.command()
async def changename(ctx, member: discord.Member, name):
    await member.edit(nick=name)
@changename.error
async def permission_error(ctx, error):
    await ctx.send("Sorry, I do not have permissions to do that!")


# works
# reset nickname of a user
@client.command()
async def resetname(ctx, member: discord.Member):
    await member.edit(nick=member.name)
    

# works
@client.command()
async def randnum(ctx, min, max):
    min = min.replace(",", "")
    min = int(min)
    max = int(max)
    shuffler = randint(min, max)
    await ctx.send("From numbers " + str(min) + " to " + str(max) + " I chose " + str(shuffler))


# works
@client.command()
async def flip(ctx):
    shuffler = randint(0, 1)
    if shuffler == 0:
        await ctx.send("Heads")
    else:
        await ctx.send("Tails")


# works
@client.command()
async def av(ctx, user:discord.Member = None):
    if (user):
        userAvatarUrl = user.avatar.url
        await ctx.send(userAvatarUrl)
    else:
        await ctx.send("Be sure to ping the target user after the command!")


# works
@client.command()
async def tictactoeinfo(ctx):
    await ctx.send(":one: :two: :three:\n"
                   ":four: :five: :six:\n"
                   ":seven: :eight: :nine:")
    

# add tic tac toe
# add music

# runs the bot
client.run(TOKEN)