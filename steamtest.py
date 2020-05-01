from __future__ import print_function

# Import steam library
from steam import SteamClient
from steam.enums.emsg import EMsg
from steam.enums import EResult
from steam.core.msg import MsgProto
from steam.client import SteamClient
from steam.enums.common import EPersonaState
from steam.client.builtins.user import User

# Create a object client
client = SteamClient()

# Function to return the numbers of the vab ban
@client.on(EMsg.ClientVACBanStatus)
def print_vac_status(msg):
    print("Number of Vac bans: %s" % msg.body.numBans)

# Try to loggin to the given credentials account
result = client.cli_login()
if result != EResult.OK:
    print("Failed to login: %s" % result)
    raise SystemExit

# Informations about the account
print("Logged on as: %s" % client.user.name)
print("State: %s" % client.user.state)
print("Community Profile: %s" % client.steam_id.community_url)
print("Last logon: %s" % client.user.last_logon)
print("Last logoff: %s" % client.user.last_logoff)

