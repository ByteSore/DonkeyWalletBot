from discord.ext import commands
from discord.utils import get
import psql
import config
import logging

class FindCog(commands.Cog):
    def __init__(self, bot):
        bot = bot

        gconf = config.global_config()

        @bot.slash_command(
            type=6,
            guild_ids=gconf['guild_ids'],
            name="betafind", 
            description="usersearch"
        )
        async def betafind(ctx, username: str = None):
            username = username

            await ctx.respond('Working on it. Check logging if necessary.', ephemeral=True)

            try:
                user_qdata = psql.select("SELECT discord_id, address FROM v2_addresses", (None,))

                '''for guild in bot.guilds:
                    for member in guild.members:
                        print(member)'''
                
                guild = bot.guilds[1]
                f = open("notfound.txt", "a+", encoding="utf-8")

                user_list = []
                for quser in user_qdata:
                    wrStr = str(quser[0])
                    if "#" in wrStr:
                        user_split = wrStr.split('#')
                        user = get(guild.members, name=user_split[0], discriminator=user_split[1])

                        if user != None:
                            f.write(wrStr + ";" + quser[1] + ";" + str(user.id) + "\n")
                        else:
                            f.write(wrStr + ";" + quser[1] + ";\n")
                    else:
                        f.write(";" + quser[1] + ";\n")
                f.close()

            except Exception as err:
                logging.error("error: " + err)

def setup(bot):
    bot.add_cog(FindCog(bot))