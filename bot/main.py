import os
import discord
from discord.ext import commands


TOKEN = os.getenv("DISCORD_TOKEN")

client = discord.Client()
      

@client.event
async def on_ready():
    print("Help Bot ready!")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='?help'))


@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.guild == None:
		return

	if message.content.startswith('?help'):
		msg = "```asciidoc\n=====================================\n= This is help message for SupportBot\n=====================================\n?help    :: This message\n \n= Transcendence wallet help =\n?download    :: Download Teloscoin wallet\n?wallet   :: How to install Teloscoin wallet\n?sync   :: Wallet sync help\n?portf   :: How to open ports on your router\n?error    :: Fix wallet errors (resync and reindex)\n?staking :: Staking info\n \n= Masternode help =\n?mninstall :: Masternode install\n?mnports   :: Check open ports on VPS\n?tiers :: Tiers info\n?roi   :: ROI info\n?10m   :: 10M info\n?support   :: Support info\n?links   :: Official & Community Transcendence links```".format(message)
		await message.channel.send(msg)

	elif message.content.startswith('?download'):
		msg = "To download the Transcendence (Teloscoin) wallet go to Github <https://github.com/phoenixkonsole/transcendence/releases> and download the most recent wallet for your OS. Latest version is 3.0.4".format(message)
		await message.channel.send(msg)

	elif message.content.startswith('?wallet'):
		msg = "Windows: Run transcendence-qt.exe and choose the folder where the blockchain will be stored, confirm and wait until the wallet sync. There is also an option to leave the default directory. For Linux users it is best to compile wallet from source for maximum performance. If you want to sync much faster you can download the most recent bootstrap. You will need to unarchive this bootstrap into your Transcendence blockchain folder.".format(message)
		await message.channel.send(msg)

	elif message.content.startswith('?sync'):
		msg = "TELOS 3.0.4 blockchain works on port 8051. You don't need to do any additional steps, just run the wallet. If for some reason the wallet won't sync check if you have the latest TELOS wallet. To help you sync faster you can also download the bootstrap which can be found on #announcement channel.".format(message)
		await message.channel.send(msg)

	elif message.content.startswith('?portf'):
		msg = "Go to <https://portforward.com/router.htm>, find your modem/router model and follow steps to port forwarding.\nCheck if port 8051 is open on <https://portchecker.co/>".format(message)
		await message.channel.send(msg)			

	elif message.content.startswith('?error'):
		msg = "If you have problems with receiving coins and txid, one of those options can be used : -rescan or -reindex (rereading blocks from start). Use -resync only if you want to rebuild blockchain from scratch.".format(message)
		await message.channel.send(msg)

	elif message.content.startswith('?staking'):
		msg = "Criterias before you can get staking coins. -You need at least 1000 unlocked coins in your wallet -Your wallet need to be on Staking active (encrypted & unlocked for staking) -Your wallet is automatically staking, as long as it is Synced.".format(message)
		await message.channel.send(msg)

	elif message.content.startswith('?mninstall'):
		msg = "If you want simplified installation of masternode please follow detailed guide from Telos official forum: <https://forum.teloscoin.org/forum/education/513-teloscoin-masternode-installation-tutorial>".format(message)
		await message.channel.send(msg)


	elif message.content.startswith('?mnports'):
		msg = "To check open ports on your server type\n```ufw status```To add port for listen\n```ufw allow 8051/tcp```".format(message)
		await message.channel.send(msg)


	elif message.content.startswith('?tiers'):
		msg = "TELOS 3.0.4 fork have masternode collaterals:\n-100k\n-300k\n-1kk (1 million)\n-3kk (3 million)\n-10kk (10 million)".format(message)
		await message.channel.send(msg)


	elif message.content.startswith('?roi'):
		msg = "To see the most accurate stats concerning the ROIs, rewards frequencies and first reward delays for Telos masternodes, please check <https://masternodestats.info/> - The ROI you will see on other websites might be totally misleading. We have contacted those websites many times, but they don't seem so eager to solve the issue on their side, that's why one faithful member of our community decided to create his own accurate platform. Also, bear in mind that ANY kind of ROI you will see is nothing but an `instant snapshot`. A 50% yearly ROI now doesn't mean you will have 50% more coins at the end of the year by launching a node now. Because every node that is added to or withdrawn from the network will change this ROI (the more nodes are added, the more the rewards are `spread` so the lesser the ROI). The `real` ROI also has to take into consideration the natural growth of the coin (feel free to check the historic graphs for Telos, you'll find out that there's much more to it than just nodes `dry ROI`.".format(message)
		await message.channel.send(msg)

	elif message.content.startswith('?10m'):
		msg = "Every tier works on the basis of the 10M tier (the King) For instance, if the 10M nodes receives, at one point, their first reward 4 days after first launch and then every 1.5 days, then the other tiers will see their delays multiplied accordingly. 100k node will have 100x more delayed rewards than 10M. Everyday new nodes join the network, so those delays get longer and longer...".format(message)
		await message.channel.send(msg)


	elif message.content.startswith('?support'):
		msg = "If you need any kind of support or have any questions concerning the project and the services, you have those options:\n- you can ask here on this discord\n- you can ask on the official Forum <https://forum.teloscoin.org/>\n- ONLY IF YOU HAVE A QUESTION RELATED TO ONE OF THE SERVICES : blueboxes, Bitdorado, peertoro contracts, AML-now etc. you can open a support ticket at <https://peertoro.eu/>\n- In every case to ensure that we will be able to help you efficiently please make sure that you give as much info as possible about your concern or issue (computer characteristics, OS, actions done and results...)".format(message)
		await message.channel.send(msg)


	elif message.content.startswith('?links'):
		msg = "Official & Community Transcendence links:\n<https://telosgreen.org> - Official website\n<https://forum.teloscoin.org> - Official forum\n<https://github.com/phoenixkonsole/transcendence> - Official GitHub\n<https://bitcoin-subsidium.org> - Official BitcoinSubsidium\n<https://governance.rocks> - Official Governance\n<https://bitstreams.tv> - Video & Stream platform\n<https://masternodestats.info> - Masternode Statistics\n<https://explorer.teloscoin.org> - Telos explorer\n<https://explorer.bitcoin-subsidium.org> - XBTX explorer\n<https://discord.gg/ykFdsHD> - Community discord\n<https://t.me/teloscointranscendenceblockchain> - English Telegram\n<https://t.me/telosturkey> - Turkish Telegram\n<https://telosnews.com> - Telos news\n<https://cryptoacid.wordpress.com> - Telos articles".format(message)
		await message.channel.send(msg)


if __name__ == "__main__":
	client.run(TOKEN)
