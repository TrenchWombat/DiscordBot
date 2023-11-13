from discord.ext import commands

bot =commands.Bot(command_prefix='!')

@bot.command()
async def info(ctx):
    """
    Display user info
    """
    await ctx.send(ctx.guild)
    await ctx.send(ctx.author)
    await ctx.send(ctx.message.id)
@bot.command()
async def punch(ctx, *args):
    """
    punch as many as you like
    """
    everyone = ' '.join(args)
    await ctx.send(f'Punched {everyone}')

bot.run('MTE3MzM3MjI1Nzk2MDIwMjMxMQ.Giw-2N.FuG8MH_lPbGKZHdDCb7ayjaemMu06rDRgmroBw')