import sys

def decrypt(msg):
    enc = msg.split('A')[:-1]
    key = "815912190485912190315912190585918159121904859121903159121905859181591219048591219031591219058591"

    dec = ""
    for i, c in enumerate(enc):
        j = (i % len(key)) + 1
        dec += chr(int(c)-1 ^ ord(key[j]))

    creds = dec.split(';')
    return creds

if __name__ == "__main__":
    msg = sys.argv[1]
    creds = decrypt(msg)
    print(f"Username: {creds[0]}\nPassword: {creds[1]}")
