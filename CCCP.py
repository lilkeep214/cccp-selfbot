import discord
from discord.ext import commands

client = commands.Bot(command_prefix=".", self_bot=True, help_command=None)
token = "VOTRE TOKEN"

@client.event
async def on_ready():
    print("CCCP SELFBOT IS READY TO WAR")

@client.command()
async def spam(ctx):
    print("Spam command")
    while True:
        await ctx.send("@everyone LA TEAM FOURCHETTE PD PD")
        await ctx.send("@everyone LA TEAM FOURCHETTE PD PD")
        await ctx.send("@everyone LA TEAM FOURCHETTE PD PD")
        await ctx.send("@everyone LA TEAM FOURCHETTE PD PD")
        await ctx.send("@everyone LA TEAM FOURCHETTE PD PD")
        await ctx.send("@everyone LA TEAM FOURCHETTE PD PD")
        await ctx.send("@everyone LA TEAM FOURCHETTE PD PD")
        await ctx.send("@everyone LA TEAM FOURCHETTE PD PD")

@client.command()
async def cccp(ctx):
    await ctx.send("CCCP SelfBot ⚜ | made by ||<@905931030626697216>|| | V1.0.1 | Profile : || __**ONLY FOR CAMARADS**__ || | discord.gg/3snYSQbV3f")

@client.command()
async def kitten(ctx):
    await ctx.send("https://tenor.com/view/kitten-cute-adorable-cat-gif-12064725")

@client.command()
async def katyusha(ctx):
    print("katyusha raid command")
    while True:
        await ctx.send("https://tenor.com/view/katyusha-gif-18144996")

@client.command()
async def r1s(ctx):
    await ctx.send("https://tenor.com/view/risitas-main-dent-issou-laugh-gif-9505807")

@client.command()
async def r2s(ctx):
    await ctx.send("https://tenor.com/view/lol-risa-risitas-laught-jaja-gif-14980369")

@client.command()
async def r3s(ctx):
    await ctx.send("https://tenor.com/view/kekw-risitas-paelleras-e-tu-juan-joya-borja-gif-22795376")

@client.command()
async def r4s(ctx):
    await ctx.send("https://tenor.com/view/el-risitas-come-on-come-on-man-mustache-serious-gif-17362553")

@client.command()
async def r5s(ctx):
    await ctx.send("https://tenor.com/view/issou-gif-7315327")

@client.command()
async def help(ctx):
    await ctx.send("**HELP COMMANDS**\n1- `spam` / spam *`@everyone`*\n2- `cccp` / See Bot statut\n3- `katyusha` / spam katyusha gif\n4 `r1s | r2s | r3s | r4s | r5s`\n 1 = rire\n 2 = méga fou-rire\n 3 = commence à rire\n 4 = il est con\n 5 = ISSOU\n PREFIX : `.` ")

client.run(token, bot=False)