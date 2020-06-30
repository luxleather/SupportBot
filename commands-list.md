**?download**
"To download the Transcendence (Teloscoin) wallet go to Github <https://github.com/phoenixkonsole/transcendence/releases> and download the most recent wallet for your OS"

**?wallet**
"Windows: Run transcendence-qt.exe and choose the folder where the blockchain will be stored, confirm and wait until the wallet sync. There is also an option to leave the default directory.
For Linux users it is best to compile wallet from source for maximum performance.
If you want to sync much faster you can download the most recent bootstrap, which can be found in the latest release files. You will need to unarchive this bootstrap into your Transcendence blockchain folder."

**?sync**
"TELOS 3.0 blockchain works on port 8051. You don't need to do any additional steps, just run the wallet. If for some reason the wallet won't sync check if you have the latest TELOS wallet"

**?portf**

"Go to <https://portforward.com/router.htm>, find your modem/router model and follow the steps for port forwarding.
Check if port 8051 is open on <https://portchecker.co/>"		

**?error**

"If you have problems with receiving coins and txid, one of those options can be used : -rescan or -reindex (rereading blocks from start). Use -resync only if you want to rebuild blockchain from scratch."

**?staking**

"Criterias before you can get staking coins.
-You need at least X unlocked coins in your wallet
-Your wallet need to be on "Staking active" (encrypted & unlocked for staking)
-Your wallet is automatically staking, as long as it is Synced
*More info:*
<https://teloscoin.org/wiki/index.php/Wallet#Status_Indicators_and_Staking>"

**?mninstall**

If you want simplified installation of maternode please follow detailed guide from Telosgreen official website: https://telosgreen.org/EN/gettingstarted/setupofnodes/

**?mnstats**

Masternode Commands:
replace word ALIAS with the name of your Master Node. as example, if name is MN01, then you would use "MN01_status".

ALIAS_start - Start masternode
ALIAS_restart - Restart masternode
ALIAS_status - Masternode status
ALIAS_stop - Stop masternode
ALIAS_config - View/Edit config file
ALIAS_getinfo - Block count/No. of connections
ALIAS_getpeerinfo - Stats of connected peers
ALIAS_resync - Resync mn wallet
ALIAS_reindex - Reindex mn wallet

If commands wont' work type 'source .bashrc'


**?mnports**

"To check for open ports on your server type
'ufw status' To add port for listen
'ufw allow 8051/tcp'

**?tiers**
TELOS 3.0 fork bring new masternode collateral:
-100k
-300k
-1kk (1 million)
-3kk (3 million)
-10kk (10 million)

**?telos3**
What is new in TELOS 3.0:
- CSV export can be found in Settings
- Added halving to 50 TELOS at block 1018866
- Added collateral change to Tiers 100K / 300K / 1M / 3M / 10M
- Added new spork and checks against Fakenodes and Stake attacks (new consensus doesnt allow to receive Stake and MN reward in the same block for the same reward)
- Wallet enforces users to add Encryption
- Masternodeprivkeys are now stored in wallet and not in transcendence.conf
- Wallet.dat is obfuscated randomly to prevent malware from finding it - Convetional Wallet.dat can be exported as file in order to move to another machine
- Explanation why we do this kind of Fraud Prevention at first startup
- IPv6 support has been dropped
- Backup the passphrase via email


**?roi**

"To see the most accurate stats concerning the ROIs, rewards frequencies and first reward delays for Telos masternodes, please check <https://masternodestats.info/> - The ROI you will see on other websites might be totally misleading. We have contacted those websites many times, but they don't seem so eager to solve the issue on their side, that's why one faithful member of our community decided to create his own accurate platform. Also, bear in mind that ANY kind of ROI you will see is nothing but an `instant snapshot`. A 50% yearly ROI now doesn't mean you will have 50% more coins at the end of the year by launching a node now. Because every node that is added to or withdrawn from the network will change this ROI (the more nodes are added, the more the rewards are `spread` so the lesser the ROI). The `real` ROI also has to take into consideration the natural growth of the coin (feel free to check the historic graphs for Telos, you'll find out that there's much more to it than just nodes `dry ROI`."

**?100k**

"Every tier works on the basis of the 100k tier (the `King`) (the "new King" will be 10M after the July fork). For instance, if the 100k nodes receives, at one point, their first reward 4 days after first launch and then every 1.5 days, then the other tiers will see their delays multiplied accordingly. 1k node will have 100x more delayed rewards than 100k. Everyday new 100k nodes join the network, so those delays get higher and higher..."

**?bitdorado**

"NOTE : Bitdorado is now closed to new members, only open for existing members until further notice---
If you have `small bags` (= under 100k) the very best and almost only viable option is to place your coins on the Bitdorado Pool (NEWBY pool, minimum deposit 1000, maximum 5000). This will give you the best return with your small bag, because Bitdorado contains the highest amount of staking Telos, so it `sucks` almost all the staking rewards from the network :) You can feel uncomfortable with sending your coins away to another person, but bear in mind that Bitdorado is Transcendence / Telos own project, lead by Pascal Papara."

**?fork**

"The TelosCoin yearly fork happens at block 1018866. It's on the 2nd of July. This fork will see the following important changes:
-block rewards halving from 100 to 50 per block
-masternodes/staking splitt doesn't change
-masternode tiers are modified as following : first tier 100k, 300k, 1M, 3M and 10M
-the wallet & daemon you need to run after the fork is the 2.1.0.0b. If your wallet & nodes are 100k tiers, already using 2.1.x.x daemon and you don't want to use a different tier you can just leave everything running.
Please ensure to be at least on wallet 2.1 at that date.."

**?support**

"If you need any kind of support or have any questions concerning the project and the services, you have those options:
-you can ask here on this discord
-you can ask on the official Forum https://forum.teloscoin.org/
-ONLY IF YOU HAVE A QUESTION RELATED TO ONE OF THE SERVICES : blueboxes, Bitdorado, peertoro contracts, AML-now etc. you can open a support ticket at https://peertoro.eu/
-In every case to ensure that we will be able to help you efficiently please make sure that you give as much info as possible about your concern or issue (computer characteristics, OS, actions done and results...)"

**?links**
Official & Community Transcendence links:
https://telosgreen.org - Official website
https://forum.teloscoin.org - Official forum
https://github.com/phoenixkonsole/transcendence - Official GitHub
https://bitcoin-subsidium.org - Official BitcoinSubsidium
https://governance.rocks - Official Governance
https://bitstreams.tv - Video & Stream platform
https://masternodestats.info - Masternode Statistics
https://explorer.teloscoin.org - Telos explorer
https://explorer.bitcoin-subsidium.org - XBTX explorer
https://discord.gg/ykFdsHD - Community discord
https://t.me/teloscointranscendenceblockchain - English Telegram
https://t.me/telosturkey - Turkish Telegram
https://telosnews.com - Telos news
https://cryptoacid.com - Telos articles
