from scapy.all import rdpcap
from scapy.layers.http import HTTPRequest
from decode import decrypt
import sys
import re

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} file")
    sys.exit(1)

last = ""
for p in rdpcap(sys.argv[1]):
    data = re.search(r'Reponse=([A-Z0-9]+)', str(p['Raw'])).group(1)
    if last != data:
        last = data
        creds = decrypt(data)
        print(f"Username: {creds[0]}\nPassword: {creds[1]}\n")
