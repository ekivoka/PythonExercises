from simplecrypt import encrypt, decrypt

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()
    print(encrypted)
       
with open("passwords.txt","r") as passes:
    for p in passes:
        p = p.rstrip('\n')
        print(p)
        try:
            s = decrypt(p, encrypted)
            break
        except Exception:
            continue
        print(s)
        print(s.decode('utf8'))
