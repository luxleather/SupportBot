**?download**

"To download the Transcendence (Teloscoin) wallet go to Github <https://github.com/phoenixkonsole/transcendence/releases> and download the most recent wallet for your OS"

**?winstall**

"Windows: Run transcendence-qt.exe and choose the folder where the blockchain will be stored, confirm and wait until the wallet syncs. There is also an option to leave the default directory.
For Linux users it is best to compile wallet from source for maximum performance.
If you want to sync much faster you can download the most recent bootstrap, which can be found in the latest release files. You will need to unarchive this bootstrap into your Transcendence blockchain folder."

**?wsync**

"TELOS 2.0 blockchain works on port 8051. You don't need to do any additional steps, just run the wallet. If for some reason the wallet won't sync check if you have the latest TELOS 2.1.0.0b version with DNS-SEEDER"

**?portf**

"Go to <https://portforward.com/router.htm>, find your modem/router model and follow the steps for port forwarding.
Check if port 8051 is open on <https://portchecker.co/>"		

**?werror**

"If you have problems with receiving coins and txid, one of those options can be used : -rescan or -reindex (rereading blocks from start). Use -resync only if you want to rebuild blockchain from scratch. (Keep in mind that you NEED to backup your wallet.dat)"

**?staking**

"Criterias before you can get staking coins.
-You need at least 1000 unlocked coins in your wallet
-Your wallet need to be on "Staking active" (encrypted & unlocked for staking)
-Your wallet is automatically staking, as long as it is Synced
*More info:*
<https://teloscoin.org/wiki/index.php/Wallet#Status_Indicators_and_Staking>"

**?mninstall**

"If you want simplified installation of maternode you can use the latest installation script
wget https://raw.githubusercontent.com/lobomfz/Masternode-tools/master/lobohub.sh && chmod +x lobohub.sh
To use it run
./lobohub.sh
The script provides fast and secure installation of masternodes with many additional options.***Credits to Lobo***"

**?mnstats**

"Script commands for easy health checking of your MN (using lobo's script):
ALIAS_start - Start masternode
ALIAS_restart - Restart masternode
ALIAS_status - Masternode status
ALIAS_stop - Stop masternode
ALIAS_config - View/Edit config file
ALIAS_getinfo - Block count/No. of connections
ALIAS_getpeerinfo - Stats of connected peers
ALIAS_resync - Resync mn wallet
ALIAS_reindex - Reindex mn wallet
If commands won't work type 'source .bashrc'"


**?mnports**

"To check for open ports on your server type
'ufw status' To add port for listen
'ufw allow 8051/tcp'

**?1k**

"Contrary to the stats you can see on some masternodes platforms such as MNO, the ROI for the first tier nodes (1000 telos or 100k after July fork) is not 4000%  or anything crazy like that... It's much less, really. + with the incoming fork in July and the first reward delay, you will most probably not receive one single reward before your node gets invalid because of the fork. So it's better to get a bit more than 1k (if you get 5k you can join the Bitdorado Pool and stake your coins there)."

**?roi**

"To see the most accurate stats concerning the ROIs, rewards frequencies and first reward delays for Telos masternodes, please check <https://masternodestats.info/> - The ROI you will see on other websites might be totally misleading. We have contacted those websites many times, but they don't seem so eager to solve the issue on their side, that's why one faithful member of our community decided to create his own accurate platform. Also, bear in mind that ANY kind of ROI you will see is nothing but an `instant snapshot`. A 50% yearly ROI now doesn't mean you will have 50% more coins at the end of the year by launching a node now. Because every node that is added to or withdrawn from the network will change this ROI (the more nodes are added, the more the rewards are `spread` so the lesser the ROI). The `real` ROI also has to take into consideration the natural growth of the coin (feel free to check the historic graphs for Telos, you'll find out that there's much more to it than just nodes `dry ROI`."

**?100k**

"Every tier works on the basis of the 100k tier (the `King`) (the "new King" will be 10M after the July fork). For instance, if the 100k nodes receives, at one point, their first reward 4 days after first launch and then every 1.5 days, then the other tiers will see their delays multiplied accordingly. 1k node will have 100x more delayed rewards than 100k. Everyday new 100k nodes join the network, so those delays get higher and higher..."

**?fork**

"In July (on block 1018866) there will be a fork which changes the global block rewards down to 50 (compared to 100 now), and will enforce the update of all the nodes in the network, and also new collaterals. The 1k, 3k, 10k and 30k collaterals won't exist anymore. They will be replaced by 100k (new minimum), 300k, 1kk 3kk and 10kk tiers."	

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
