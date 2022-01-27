import discord
import csv

def wallet_check(message):
    msgsplit = message.content.split(' ')
    wallet_addr = msgsplit[1]
    if wallet_addr.startswith('0x') and len(wallet_addr) == 42:
        return True
    return False

def register_wallet(message):
    msgsplit = message.content.split(' ')
    wallet_addr = msgsplit[1]
    csv_file = open("app/wallets.csv", "a+")
    csv_prep_line = wallet_addr + ";" + "{0.author}".format(message)
    csv_file.write(csv_prep_line + "\n")
    csv_file.close()

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    full_disc_name = "{0.author.name}#{0.author.discriminator}".format(message)
        
    ##############################################
    ## HELP
    ##############################################
    if message.content == "!register" or message.content == "!update":
        await message.channel.send('```Usage:\n!register <wallet_address>    // To register your wallet\n!update <wallet_address>      // To register your wallet\n!check                        // To check your registration```')
        
    ##############################################
    ## CHECK
    ##############################################
    if message.content == "!check":

        found = 0
        with open('app/wallets.csv') as f:
            if full_disc_name in f.read():
                found = 1
        
        if found == 1:
            await message.channel.send('<@{0.author.id}>, your wallet is stored in our database.'.format(message))
        else:
            await message.channel.send('<@{0.author.id}>, could not find your wallet. Please use !register to save it.'.format(message))

    ##############################################
    ## UPDATE
    ##############################################
    if message.content.startswith('!update '):

        if wallet_check(message):

            found = 0
            i=0
            with open('app/wallets.csv') as f:
                lines = f.readlines()

            with open('app/wallets.csv', "w") as f:
                for line in lines:
                    if not full_disc_name in line:
                        f.write(line)
            
            register_wallet(message)
            await message.channel.send('Thanks <@{0.author.id}>. Your wallet has been updated.'.format(message))

            await message.delete()
        else:
            await message.channel.send('<@{0.author.id}>. Your wallet has is not of a correct format.'.format(message))

    ##############################################
    ## REGISTER
    ##############################################
    if message.content.startswith('!register '):
        
        if wallet_check(message):
            found = 0
            with open('app/wallets.csv') as f:
                if full_disc_name in f.read():
                    found = 1
            
            if found == 1:
                await message.channel.send('<@{0.author.id}>, your wallet has already been saved. To change your wallet, please use !update.'.format(message))
            else:
            
                register_wallet(message)
                await message.channel.send('Thanks <@{0.author.id}>. Your wallet has been updated.'.format(message))

                await message.delete()
                await message.channel.send('Thanks <@{0.author.id}>. Your wallet is saved.'.format(message))
        else:
            await message.channel.send('<@{0.author.id}>. Your wallet has is not of a correct format.'.format(message)) 

client.run('OTM1Njk5NDQzODU1MDAzNjc5.YfCcAw.N-PAcL7WzynJgr1DEcqwRWxnc0I')
