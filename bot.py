import discord
from discord.ext import commands
client = commands.Bot(command_prefix="!")
@client.event
async def on_ready():
    print ("Bot is ready")

@client.command()
async def hello(ctx):
   await ctx.send("Hi,how are ya?")


@client.command()
async def kick(ctx , member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
async def ban(ctx , member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')
    
@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for banned_entry in banned_users:
        user = banned_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

@client.command()
async def say(ctx, *, arg):
    await ctx.send (f"{arg}\n"
    "** **\n"
    f"{ctx.author.mention}\n")
