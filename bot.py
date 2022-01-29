import discord
from discord.ext import commands
import psql
import logging

bot = discord.Bot()

'''
@bot.event
async def on_ready():
    await config.ensure_db_pool_is_initialized()
'''

@bot.slash_command(guild_ids=[932672283321966602], name="check", description="command to check the wallet")
async def check(ctx, wallet: str):
    wallet = wallet
   
    try:
        check_data = psql.selectone("SELECT address FROM v2_addresses WHERE address = %s", (wallet,))

        if check_data is None or check_data is []:
            await ctx.respond('Sorry, <@{0.author.id}>... you aren\'t whitelisted (yet!)'.format(ctx), ephemeral=True)
            #await ctx.respond('<@{0.author.id}>, could not find your wallet. Please use !register to save it.'.format(ctx), ephemeral=True)
        else:
            await ctx.respond('Congratulations <@{0.author.id}>! You are on the whitelist!'.format(ctx), ephemeral=True)
    except Exception:
        logging.error("error: ")


bot.run("<token>")

