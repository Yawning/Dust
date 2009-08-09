import os
import sys
# python sucks
sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), "..")))

from invite.invite import InvitePackage
from crypto.keys import KeyManager
from core.util import getAddress

password=sys.argv[1]

port=int(sys.argv[2])

v6=True # defaults to IPv6
if len(sys.argv)>3:
  if sys.argv[3]=='6':
    v6=True
  elif sys.argv[3]=='4':
    v6=False
  else:
    print('Unknown IP version:', sys.argv[2])

if v6:
  print('Generating invites for udp://'+getAddress(port))
else:
  print('Generating invites for udp://'+getPublicIP()+':'+str(port))
    
keys=KeyManager()
keys.loadKeypair('config/id.yaml')
keypair=keys.getKeypair()
pubkey=keypair.public

ip=InvitePackage()
ip.generate(pubkey, v6, False, port, 5, keys.entropy)
ip.save('config/incoming_invites.ip', password, keys.entropy)
