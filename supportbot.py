#!/usr/bin/python

import discord
from discord.ext import commands

token = "TOKEN"

client = discord.Client()       

@client.event
async def on_ready():
    print("SupportBot ready!")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='?help'))


@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.guild == None:
		return

	if message.content.startswith('?help'):
		msg = "```asciidoc\n=====================================\n= This is help message for SupportBot\n=====================================\n?help    :: This message\n \n= Transcendence wallet help =\n?download    :: Download Teloscoin wallet\n?wallet   :: How to install Teloscoin wallet\n?sync   :: Wallet sync help\n?portf   :: How to open ports on your router\n?error    :: Fix wallet errors (resync and reindex)\n?staking :: Staking info\n?telos3 :: What's new in TELOS 3.0\n \n= Masternode help =\n?mninstall :: Masternode install\n?mnstats  :: Masternode status after install\n?mnports   :: Check open ports on VPS\n?tiers :: Tiers info\n?roi   :: ROI info\n?100k   :: 100k info\n?fork   :: Fork info\n?bitdorado   :: Bitdorado info\n?support   :: Support info\n?links   :: Official & Community Transcendence links```".format(message)
		await message.channel.send(msg)

	elif message.content.startswith('?download'):
		msg = "To download the Transcendence (Teloscoin) wallet go to Github <https://github.com/phoenixkonsole/transcendence/releases> and download the most recent wallet for your OS. At least 2.1 is recommended before fork (block 1018866)".format(message)
		await message.channel.send(msg)

	elif message.content.startswith('?wallet'):
		msg = "Windows: Run transcendence-qt.exe and choose the folder where the blockchain will be stored, confirm and wait until the wallet sync. There is also an option to leave the default directory. For Linux users it is best to compile wallet from source for maximum performance. If you want to sync much faster you can download the most recent bootstrap, which can be found in the latest release files. You will need to unarchive this bootstrap into your Transcendence blockchain folder.".format(message)
		await message.channel.send(msg)

	elif message.content.startswith('?sync'):
		msg = "TELOS 3.0 blockchain works on port 8051. You don't need to do any additional steps, just run the wallet. If for some reason the wallet won't sync check if you have the latest TELOS wallet".format(message)
		await message.channel.send(msg)

	elif message.content.startswith('?portf'):
		msg = "Go to <https://portforward.com/router.htm>, find your modem/router model and follow steps to port forwarding.\nCheck if port 8051 is open on <https://portchecker.co/>".format(message)
		await message.channel.send(msg)			

	elif message.content.startswith('?error'):
		msg = "If you have problems with receiving coins and txid, one of the options can be used -rescan or -reindex (rereading blocks from start). Button -resync use only if you want to rebuild blockchain from start. (Keep in mind that wallet.dat backup is mandatory to made.)".format(message)
		await message.channel.send(msg)

	elif message.content.startswith('?staking'):
		msg = "Criterias before you can get stake coins.\n-You need at least 1000 unlocked coins in your wallet\n-Your wallet need to be Staking active\n-Your wallet is automatically staking, as long as it is Synced\n*More info:*\n<https://teloscoin.org/wiki/index.php/Wallet#Status_Indicators_and_Staking>".format(message)
		await message.channel.send(msg)

	elif message.content.startswith('?mninstall'):
		msg = "If you want simplified installation of maternode please follow detailed guide from Telosgreen official website: <https://telosgreen.org/EN/gettingstarted/setupofnodes/>".format(message)
		await message.channel.send(msg)

	elif message.content.startswith('?mnstats'):
		msg = "Masternode Commands: replace word ALIAS with the name of your Master Node. as example, if name is MN01, then you would use MN01_status:\nALIAS_start - Start masternode\nALIAS_restart - Restart masternode\nALIAS_status - Masternode status\nALIAS_stop - Stop masternode\nALIAS_config - View/Edit config file\nALIAS_getinfo - Block count/No. of connections\nALIAS_getpeerinfo - Stats of connected peers\nALIAS_resync - Resync mn wallet\nALIAS_reindex - Reindex mn wallet\nIf commands wont' work type 'source .bashrc'".format(message)
		await message.channel.send(msg)


	elif message.content.startswith('?mnports'):
		msg = "To check open ports on your server type\n```ufw status```To add port for listen\n```ufw allow 8051/tcp```".format(message)
		await message.channel.send(msg)


	elif message.content.startswith('?tiers'):
		msg = "TELOS 3.0 fork bring new masternode collateral:\n-100k\n-300k\n-1kk (1 million)\n-3kk (3 million)\n-10kk (10 million)".format(message)
		await message.channel.send(msg)


	elif message.content.startswith('?telos3'):
		msg = "What is new in TELOS 3.0:\n- CSV export can be found in Settings\n- Added halving to 50 TELOS at block 1018866\n- Added collateral change to Tiers 100K / 300K / 1M / 3M / 10M\n- Added new spork and checks against Fakenodes and Stake attacks (new consensus doesnt allow to receive Stake and MN reward in the same block for the same reward)\n- Wallet enforces users to add Encryption\n- Masternodeprivkeys are now stored in wallet and not in transcendence.conf\n- Wallet.dat is obfuscated randomly to prevent malware from finding it - Convetional Wallet.dat can be exported as file in order to move to another machine\n- Explanation why we do this kind of Fraud Prevention at first startup\n- IPv6 support has been dropped\n-  Backup the passphrase via email".format(message)
		await message.channel.send(msg)



	elif message.content.startswith('?roi'):
		msg = "To see the most accurate stats concerning the ROIs, rewards frequencies and first reward delays for Telos masternodes, please check <https://masternodestats.info/> - The ROI you will see on other websites might be totally misleading. We have contacted those websites many times, but they don't seem so eager to solve the issue on their side, that's why one faithful member of our community decided to create his own accurate platform. Also, bear in mind that ANY kind of ROI you will see is nothing but an `instant snapshot`. A 50% yearly ROI now doesn't mean you will have 50% more coins at the end of the year by launching a node now. Because every node that is added to or withdrawn from the network will change this ROI (the more nodes are added, the more the rewards are `spread` so the lesser the ROI). The `real` ROI also has to take into consideration the natural growth of the coin (feel free to check the historic graphs for Telos, you'll find out that there's much more to it than just nodes `dry ROI`.".format(message)
		await message.channel.send(msg)

	elif message.content.startswith('?100k'):
		msg = "Every tier works on the basis of the 100k tier (the `King`) (the `new King` will be 10M after the July fork). For instance, if the 100k nodes receives, at one point, their first reward 4 days after first launch and then every 1.5 days, then the other tiers will see their delays multiplied accordingly. 1k node will have 100x more delayed rewards than 100k. Everyday new 100k nodes join the network, so those delays get higher and higher...".format(message)
		await message.channel.send(msg)

	elif message.content.startswith('?fork'):
		msg = "The TelosCoin yearly fork happens at block 1018866. It's on the 2nd of July. This fork will see the following important changes:\n- block rewards halving from 100 to 50 per block\n- masternodes/staking splitt doesn't change\n- masternode tiers are modified as following: 100k, 300k, 1M, 3M and 10M\n- the wallet & daemon you need to run after the fork is the 2.1.0.0b. If your wallet & nodes are 100k tiers, already using 2.1.x.x daemon and you don't want to use a different tier you can just leave everything running. Please ensure to be at least on wallet 2.1 at that date..".format(message)
		await message.channel.send(msg)		

	elif message.content.startswith('?bitdorado'):
		msg = "IMPORTANT NOTICE: until further notice Bitdorado pools & services are CLOSED TO NEW USERS. Only already registered users can use and deposit coins right now. If you have small bags (= under 100k) the very best and almost only viable option is to place your coins on the Bitdorado Pool (NEWBY pool - minimum 1000, maximum 5000 Teloscoins). This will give you the best return with your small bag, because Bitdorado contains the highest amount of staking Telos, so it sucks almost all the staking rewards from the network You can feel uncomfortable with sending your coins away to another person, but bear in mind that Bitdorado is Transcendence / Telos own project, lead by Pascal Papara.".format(message)
		await message.channel.send(msg)


	elif message.content.startswith('?support'):
		msg = "If you need any kind of support or have any questions concerning the project and the services, you have those options:\n- you can ask here on this discord\n- you can ask on the official Forum <https://forum.teloscoin.org/>\n- ONLY IF YOU HAVE A QUESTION RELATED TO ONE OF THE SERVICES : blueboxes, Bitdorado, peertoro contracts, AML-now etc. you can open a support ticket at <https://peertoro.eu/>\n- In every case to ensure that we will be able to help you efficiently please make sure that you give as much info as possible about your concern or issue (computer characteristics, OS, actions done and results...)".format(message)
		await message.channel.send(msg)


	elif message.content.startswith('?links'):
		msg = "Official & Community Transcendence links:\n<https://telosgreen.org> - Official website\n<https://forum.teloscoin.org> - Official forum\n<https://github.com/phoenixkonsole/transcendence> - Official GitHub\n<https://bitcoin-subsidium.org> - Official BitcoinSubsidium\n<https://governance.rocks> - Official Governance\n<https://bitstreams.tv> - Video & Stream platform\n<https://masternodestats.info> - Masternode Statistics\n<https://explorer.teloscoin.org> - Telos explorer\n<https://explorer.bitcoin-subsidium.org> - XBTX explorer\n<https://discord.gg/ykFdsHD> - Community discord\n<https://t.me/teloscointranscendenceblockchain> - English Telegram\n<https://t.me/telosturkey> - Turkish Telegram\n<https://telosnews.com> - Telos news\n<https://cryptoacid.com> - Telos articles".format(message)
		await message.channel.send(msg)	

client.run(token)
