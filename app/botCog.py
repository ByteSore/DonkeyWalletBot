from discord.ext import tasks, commands

class BotCog(commands.Cog):
    def __init__(self):
        self.index = 0
        self.guildids_update.start()

    def cog_unload(self):
        self.guildids_update.cancel()

    @tasks.loop(seconds=15)
    async def guildids_update(bot, guildIDs):
        for guild in bot.guilds:
            print(guild.id)
            if guild.id not in guildIDs:
                guildIDs.append(guild.id)
                print(guild.id)