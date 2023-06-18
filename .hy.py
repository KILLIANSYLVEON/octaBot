import discord
from discord.ext import commands, tasks
import random
import asyncio
from discord import Streaming
from discord.utils import get
from discord import app_commands
import time
import datetime
from datetime import datetime





bot = commands.Bot(command_prefix="--", intents=discord.Intents.all())

bot.remove_command("help")
#slash = SlashCommand(bot, sync_commands = True)
import typing 


 


@tasks.loop(minutes = 1, seconds = 11)
async def changeStatus():
    streamer = random.choice(["valorant.octive|--help", "ma vie de bot.octabot|--help", "ton jeux pref.toi|--help", "zelda totk.killian(二ンフㇶア)|--help"])
    await bot.change_presence(activity=discord.Streaming(name=streamer, url= "https://www.twitch.tv/botpersonaliserparkillian"))


"""

status = ["avec Octive|--help", "discord|--help", "avec moi-meme|--help", "avec toi|--help", "avec killian(ニンフィア)|--help", "ma vie de bot|--help"]







@tasks.loop(minutes = 1, seconds = 45)
async def changeStatus():
    game = discord.Game(random.choice(status))
    await bot.change_presence(status = discord.Status.online, activity = game)


"""


@bot.event
async def on_ready():
    print("bot en ligne")
    synced = await bot.tree.sync()
    print("syncroniser")
    changeStatus.start()




@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1009383466644807780)
    
    embed = discord.Embed(title = (member), description = "bienvenue a toi sur le serveur de octive m", color = 0x3377FF)
    embed.set_image(url=member.display_avatar)

    embed.add_field(name = "total des menbres", value = (member.guild.member_count))
    await channel.send(f"merci {member.mention}")


    await channel.send(embed= embed)
    guild = member.guild
    channeln = bot.get_channel(1111700846057639997)
    await channeln.edit(name = f"total des membre: {member.guild.member_count}")
    

channel = (1009383466644807780)



@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1009383466644807780)
    embed = discord.Embed(title =f"dommage {member.name}", description = "un menbre vient de nous quitter", color =0xBE2808)

    await channel.send(embed= embed)
    guild = member.guild
    channeln = bot.get_channel(1111700846057639997)
    await channeln.edit(name = f"total des membre: {member.guild.member_count}")



@bot.command()
async def help(ctx):
    help_embed = discord.Embed(title="commande help de octabot", description="ici toute les commande du bot", color=discord.Color.random())

    help_embed.add_field(name="octabot", value="je suis le bot du serveur de octivem creer par killian(二ンフㇶア)", inline=False)

    help_embed.add_field(name="--help", value="affiche ce message", inline=False)
    help_embed.add_field(name="--temps", value="donne la date et l'heure du moment", inline=False)
    help_embed.add_field(name="--timestamp", value="donne la valeur du timestamp", inline=False)
    help_embed.add_field(name="--ping", value="repond pong avec la lattetence en ms", inline=False)
    help_embed.add_field(name="--tm", value="repond le nombre de membre total sur le serveur", inline=False)
    help_embed.add_field(name="--reseaux", value="envoier le lien des reseaux de octive", inline=False)
    help_embed.add_field(name="--ing", value="envoie ong", inline=False)
    help_embed.add_field(name="--salut", value="le bot envoie salut", inline=False)
    help_embed.add_field(name="slash commande", value="les commande se fesant avec un /", inline=False)
    help_embed.add_field(name="/multiplication", value="pour pouvoir multiplier 2 nombres", inline=False)
    help_embed.add_field(name="/dividion", value="pour diviser 2 nombres", inline=False)
    help_embed.add_field(name="/addition", value="pour faire une addition", inline=False)
    help_embed.add_field(name="/soustraction", value="pour soustraire 2 nombres", inline=False)

    await ctx.send(embed=help_embed)


@bot.command()
async def testvi(ctx):
    await ctx.send("fait avec visual studio code")

@bot.tree.command()
@app_commands.describe(thing_to_say = "nonbre 1", thing_to_say2 = "nonbre 2")
async def addition(interaction: discord.Interaction, thing_to_say: int, thing_to_say2: int):
    result = thing_to_say + thing_to_say2
    await interaction.response.send_message(f"le resultat de {thing_to_say} plus {thing_to_say2} est de {result}")


@bot.tree.command()
@app_commands.describe(thing_to_say = "nonbre 1", thing_to_say2 = "nonbre 2")
async def multiplication(interaction: discord.Interaction, thing_to_say: int, thing_to_say2: int):
    result = thing_to_say * thing_to_say2
    await interaction.response.send_message(f"le resultat de {thing_to_say} fois {thing_to_say2} est de {result}")



@bot.tree.command()
@app_commands.describe(thing_to_say = "nonbre 1", thing_to_say2 = "nonbre 2")
async def division(interaction: discord.Interaction, thing_to_say: int, thing_to_say2: int):
    result = thing_to_say / thing_to_say2
    await interaction.response.send_message(f"le resultat de {thing_to_say} diviser par {thing_to_say2} est de {result}")



@bot.tree.command()
@app_commands.describe(thing_to_say = "nonbre 1", thing_to_say2 = "nonbre 2")
async def soustraction(interaction: discord.Interaction, thing_to_say: int, thing_to_say2: int):
    result = thing_to_say - thing_to_say2
    await interaction.response.send_message(f"le resultat de {thing_to_say} moins {thing_to_say2} est de {result}")


@bot.tree.command(name="dire")
@app_commands.describe(thing_to_say = "que veut tu dire")
async def dit(interaction: discord.Interaction, thing_to_say: str):
    await interaction.response.send_message(f"{interaction.user.name} a dit: {thing_to_say}")
"""
@bot.command()
async def tmo(ctx, member):
    await ctx.send(f"totale des member en ligne {discord.Guild.approximate_member_count} ")
"""

@bot.command()
async def message(ctx, user:discord.Member, *, message=None):
    message = message
    await user.send(message)



@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)




@bot.command()
async def temps(ctx):
    actuel = datetime.now()
    await ctx.reply(actuel)



@bot.command()
async def ping(ctx):
    await ctx.reply(f'pong avec une latence de {round(bot.latency * 1000)}ms')

@bot.command()
async def timestamp(ctx):
    
    await ctx.send(f"le timestamp actuelle est de {time.time()} senconde ecouler depuis le 1 janvier 1970")



@bot.command()
@commands.has_permissions(manage_channels = True)
async def tchaname(ctx, channel: discord.TextChannel, *, new_name):
    await channel.edit(name=new_name)



@bot.command()
async def testem(ctx, *,member: discord.member=None):
    member = ctx.author if not member else member
    embed = discord.Embed(title ="test", description = "test et test", color = 0x9147ff)
    embed.add_field(name = "nom", value = "coucou", inline = True)

    await ctx.send(embed = embed)



@bot.command()
@commands.has_permissions(manage_channels = True)
async def voicesup(ctx, channel: discord.VoiceChannel):
    await channel.delete()



@bot.command()
@commands.has_permissions(manage_channels = True)
async def textsup(ctx, channel: discord.TextChannel):
    await channel.delete()

"""
@bot.command()
@commands.has_permissions(manage_channels= True)
async def newtc(ctx, channelName, category):
    guild = ctx.guild
    await guild.create_text_channel(name=f"{channelName}", category=category)

"""



@bot.command()
@commands.has_permissions(manage_channels = True)
async def vchaname(ctx, channel: discord.VoiceChannel, *, new_name):
    await channel.edit(name=new_name)



@bot.command()
async def tm(member):
    await member.send(f"totale des menbre sur le serveur {member.guild.member_count} menbre")





@bot.command()
async def reseaux(ctx):
    youtubel = "https://www.youtube.com/@octivem"
    twitchl = "https://www.twitch.tv/octivemytb"
    embed = discord.Embed(title = "les different lien de octive", description = f"sur youtube {youtubel}\n et aussi sur twitch {twitchl}")
    embed.set_thumbnail(url = "https://yt3.googleusercontent.com/XBJgZ63uUpvQf_imUpc6MEKg5QhLyDpA5slxf6AQZH266v5v5hgV2ZSExFV-8yndbFFPEl0lbaI=s176-c-k-c0x00ffffff-no-rj")

    await ctx.send(embed = embed)



@bot.command()

async def ing(ctx):
    await ctx.send("ong")

@bot.command()
@commands.is_owner()
async def pick(ctx):
    choisir = ["1", "2", "3"]
    await ctx.send(random.choice(choisir))




@bot.command()
async def salut(ctx):
    await ctx.reply("salut")


#member.guild.member_count
#datetime.datetime.utcnow




bot.run("TOKEN")
