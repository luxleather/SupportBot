#!/usr/bin/python

import discord
from discord.ext import commands
import asyncio

token = "TOKEN"

client = discord.Client()

async def status_task():
    while True:
        await client.change_presence(activity=discord.Game(name="?help"))
        await asyncio.sleep(20)
        await client.change_presence(activity=discord.Game(name="www.telosgreen.org"))
        await asyncio.sleep(20)
        await client.change_presence(activity=discord.Game(name="I'am in " + str(len(client.guilds)) + " servers"))
        await asyncio.sleep(20)        

@client.event
async def on_ready():
    print("SupportBot ready!")
    client.loop.create_task(status_task())


@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.guild == None:
		return

	if message.content.startswith('?help'):
		msg = "```asciidoc\n=====================================\n= This is help message for SupportBot\n=====================================\n?help    :: This message\n \n= Transcendence wallet help =\n?download    :: Download Teloscoin wallet\n?winstall   :: How to install Teloscoin wallet\n?wsync   :: Wallet sync help\n?portf   :: How to open ports on your router\n?werror    :: Fix wallet errors (resync and reindex)\n?staking :: Staking info\n \n= Masternode help =\n?mninstall :: Masternode install with LoboHub script\n?mnstats  :: Masternode status after install (sync, getinfo)\n?mnports   :: Check open ports on VPS\n?1k   :: 1k info\n?roi   :: ROI info\n?100k   :: 100k info\n?fork   :: Fork info\n?bitdorado   :: Bitdorado info```".format(message)
		await message.channel.send(msg)

	elif message.content.startswith('?download'):
		msg = "To download Transcendence (Teloscoin) wallet go to Github <https://github.com/phoenixkonsole/transcendence/releases> and download wallet for your OS".format(message)
		await message.channel.send(msg)

	elif message.content.startswith('?winstall'):
		msg = "Windows: Run transcendence-qt.exe and choose folder where blockchain will be stored, confirm and wait until wallet sync. There is also option to leave default directory.\nFor Linux users it is best to compile wallet from source for maximum performance.".format(message)
		await message.channel.send(msg)

	elif message.content.startswith('?wsync'):
		msg = "TELOS 2.0 blockchain work on port 8051. You don't need to do any additional steps just run wallet. If for some reason wallet won't sync check if you have latest TELOS 2.0.0.1 version with DNS-SEEDER".format(message)
		await message.channel.send(msg)

	elif message.content.startswith('?portf'):
		msg = "Go to <https://portforward.com/router.htm>, find your modem/router model and follow steps to port forwarding.\nCheck if port 8051 is open on <https://portchecker.co/>".format(message)
		await message.channel.send(msg)			

	elif message.content.startswith('?werror'):
		msg = "If you have problems with receiving coins and txid, one of the options can be used -rescan or -reindex (rereading blocks from start). Button -resync use only if you want to rebuild blockchain from start. (Keep in mind that wallet.dat backup is mandatory to made.)".format(message)
		await message.channel.send(msg)

	elif message.content.startswith('?staking'):
		msg = "Criterias before you can get stake coins.\n-You need at least 1000 unlocked coins in your wallet\n-Your wallet need to be Staking active\n-Your wallet is automatically staking, as long as it is Synced\n*More info:*\n<https://teloscoin.org/wiki/index.php/Wallet#Status_Indicators_and_Staking>".format(message)
		await message.channel.send(msg)

	elif message.content.startswith('?mninstall'):
		msg = "Use latest installation script```\nwget https://raw.githubusercontent.com/lobomfz/Masternode-tools/master/lobohub.sh && chmod +x lobohub.sh```To use it run```\n./lobohub.sh```Script provide fast and secure installation of masternodes with many additional options.\n***Credits to Lobo***".format(message)
		await message.channel.send(msg)

	elif message.content.startswith('?mnstats'):
		msg = "Script commands for easy checking health of your MN:\nALIAS_start - Start masternode\nALIAS_restart - Restart masternode\nALIAS_status - Masternode status\nALIAS_stop - Stop masternode\nALIAS_config - View/Edit config file\nALIAS_getinfo - Block count/No. of connections\nALIAS_getpeerinfo - Stats of connected peers\nALIAS_resync - Resync mn wallet\nALIAS_reindex - Reindex mn wallet\nIf commands wont' work type 'source .bashrc'".format(message)
		await message.channel.send(msg)


	elif message.content.startswith('?mnports'):
		msg = "To check open ports on your server type\n```ufw status```To add port for listen\n```ufw allow 8051/tcp```".format(message)
		await message.channel.send(msg)		

	elif message.content.startswith('?1k'):
		msg = "Contrary to the stats you can see on some masternodes platforms such as MNO, the ROI for the first tier nodes (1000 telos) is not 4000%  or anything crazy like that... It's much less, really. + with the incoming fork in July and the first reward delay, you will most probably not receive one single reward before your node gets invalid because of the fork. So it's better to get a bit more than 1k (if you get 5k you can join the Bitdorado Pool and stake your coins there).".format(message)
		await message.channel.send(msg)

	elif message.content.startswith('?roi'):
		msg = "To see the most accurate stats concerning the ROIs, rewards frequencies and first reward delays for Telos masternodes, please check <https://masternodestats.info/> - The ROI you will see on other websites might be totally misleading. We have contacted those websites many times, but they don't seem so eager to solve the issue on their side, that's why one faithful member of our community decided to create his own accurate platform. Also, bear in mind that ANY kind of ROI you will see is nothing but an `instant snapshot`. A 50% yearly ROI now doesn't mean you will have 50% more coins at the end of the year by launching a node now. Because every node that is added to or withdrawn from the network will change this ROI (the more nodes are added, the more the rewards are `spread` so the lesser the ROI). The `real` ROI also has to take into consideration the natural growth of the coin (feel free to check the historic graphs for Telos, you'll find out that there's much more to it than just nodes `dry ROI`.".format(message)
		await message.channel.send(msg)

	elif message.content.startswith('?100k'):
		msg = "Every tier works on the basis of the 100k tier (the `King`). For instance, if the 100k nodes receive, at one point, their first reward 4 days after first launch and then every 1.5 days, then the other tiers will see their delays multiplied accordingly. 1k node will have 100x more delayed rewards than 100k. Everyday new 100k nodes join the network, so those delays get higher and higher...".format(message)
		await message.channel.send(msg)

	elif message.content.startswith('?fork'):
		msg = "In July (precise date to be determined) there will be a fork which changes the block rewards down to 50 (compared to 100 now), and will enforce the update of all the nodes in the network, and also new collaterals. The 1k, 3k, 10k and 30k collaterals won't exist anymore. They will be replaced by 100k (new minimum), 300k, 1kk 3kk and 10k tier.".format(message)
		await message.channel.send(msg)		

	elif message.content.startswith('?bitdorado'):
		msg = "If you have `small bags` (= under 100k) the very best and almost only viable option is to place your coins on the Bitdorado Pool. This will give you the best return with your small bag, because Bitdorado contains the highest amount of staking Telos, so it `sucks` almost all the staking rewards from the network :) You can feel uncomfortable with sending your coins away to another person, but bear in mind that Bitdorado is Transcendence / Telos own project, lead by Pascal Papara.".format(message)
		await message.channel.send(msg)		

client.run(token)
