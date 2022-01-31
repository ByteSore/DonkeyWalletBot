from discord.ext import commands
from discord.utils import get
import psql
import config
import logging
from pprint import pprint

class CheckCog(commands.Cog):
    def __init__(self, bot):
        bot = bot

        gconf = config.global_config()

        @bot.slash_command(guild_ids=[932672283321966602], name="betacheck", description="command to check the wallet")
        async def betacheck(ctx, wallet: str):
            wallet = wallet
        
            try:
                check_data = psql.selectone("SELECT address FROM v2_addresses WHERE address ILIKE %s", (wallet,))

                if check_data is None or check_data is []:
                    await ctx.respond('Sorry, <@{0.author.id}>... you aren\'t whitelisted (yet!)'.format(ctx), ephemeral=True)
                    #await ctx.respond('<@{0.author.id}>, could not find your wallet. Please use !register to save it.'.format(ctx), ephemeral=True)
                else:
                    await ctx.respond('Congratulations <@{0.author.id}>! You are on the whitelist!'.format(ctx), ephemeral=True)
            except Exception as err:
                logging.error("error: " + err)


        bot.run("OTM1Njk5NDQzODU1MDAzNjc5.YfCcAw.IULfQZ1Y0cudN1X9OUv-H-0w3dQ")

def setup(bot):
    bot.add_cog(CheckCog(bot))