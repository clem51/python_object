import re
import binascii

with open ("obfusced.js", "r") as f :
    raw = f.read()
    find = list(dict.fromkeys(re.findall(r"\\x[0-9a-z]{2}", raw)))
    for hexa in find :
        char = chr(int(hexa[2:], base = 16))
        raw = raw.replace(hexa, char)
    with open ("dezob.js", "w") as f2 :
        f2.write(raw)
    


    