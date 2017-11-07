import json
import hashlib
import random
import base64

copyright = """"
Copyright 2017 James Construct

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


def CreateKey(s, salt="si4kth4g36we8h4m6s5qe87gh0df10"):
    if (len(s) < 8):
        print("ERROR! Key has to be longer than eight letters or equal.")
        return None
    s, control = EditInput(s, salt)
    key_fin = ""
    for CurrentS in s:
        key_sha = hashlib.sha512((CurrentS + control).encode("utf-8")).hexdigest()
        blocks = []
        key = ""
        for i in range(16):
             blocks.append(key_sha[i*8:(i*8+8)])
        n = ord(CurrentS[0]) % 8
        for i in blocks:
            key += i[n]
            n = ord(i[n]) % 8
        key_fin += key
    return key_fin

def EditInput(s, salt):
    s += "Just salt here:" + salt # add salt
    control_hash = hashlib.sha1(s.encode("utf-8")).hexdigest()
    s_rev = s[::-1] # reverse string
    s_fin = ""
    for i in range(len(s)):
        s_fin += s[i] + s_rev[i] # put reversed and normal to getheader
    l = len(s_fin)
    b_s = l // 8
    s_array = []
    for i in range(b_s):
        s_array.append(s_fin[i*4:(i*4+8)])
    #control_hash *= l // 40 + 1
    return s_array, control_hash

def Encrypt(s, key, Difficulty=1.0):
    try:
        Words = loadList()
    except:
        createWordlist()
        Words = loadList()

    s += "ǂ" * (64-len(s)%64) # create a string with length, which is multiple of 64
    digest = []
    WordDigest = []
    for i in range(len(s)):
        digest.append((ord(s[i]) + ord(key[i%len(key)])))
    for i in digest:
        WordDigest.append(Words[i])

    return "".join(WordDigest)

def Decrypt(Msg, key, Difficulty=1.0):
    try:
        Words = loadList()
    except:
        createWordlist()
        Words = loadList()

    s = ""
    n = 0
    for i in range(int(len(Msg)/5)):
        try:
            s += chr(int(Words.index(Msg[n:n+5]) - ord(key[i%len(key)])))
            n += 5
        except ValueError:
            pass
    s = s.replace("ǂ", "") # filter filling
    return s

def createWordlist():
    data = []
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFHJIJKLMNOPQRSTUVWXYZ"
    for i in range(10000):
        d = ""
        for y in range(5):#random.randint(2, 5)):
            d += random.choice(alphabet)
        if d not in data:
            data.append(d)
    data = list(set(data))
    tw = json.dumps(data, sort_keys=True, indent=4)
    f = open("Words.json", "w")
    f.write(tw)
    f.close()

def loadList():
    try:
        f = open("Words.json", "r")
    except:
        createWordlist()
        return False
    Words = json.loads(f.read())
    f.close()
    return Words


def Translate(s, mode="in"):
    if mode is "in":
        return base64.b64encode(s).decode()
    elif mode is "out":
        return base64.b64decode(s)
    else:
        print("Value error! Mode must be set to 'in' or 'out'!")
        return

def Help():
    help = "***PCA - Portable Crypting Algorithm***\n" \
           "        Author: James Contruct (call Copyright() for more info)\n" \
           "Public functions: \n" \
           "\tCreateKey(string, salt=optional)\n" \
           "\t\tCreates crypting key from used string and salt. Minimum length is 8, minimum recommended is 16. \n" \
           "\tEncrypt(string, key, difficulty=1)\n" \
           "\t\tEncrypt string with key. Returns string. Difficulty is optional argument, have to be positive float. If not set - 1. To turn off counting with difficulty set to 0.\n" \
           "\tDecrypt(string, key, difficulty=1)\n" \
           "\t\tDecrypt string with key. Returns string. Difficulty have to be the same as used while encrypting!\n" \
           "\tTranslate(string, mode)\n" \
           "\t\tTranslate bytes to b64. Is used to translate picture (or any other file, except text) to b64. Mode have to be 'in' or 'out'. In - string->b64, out - b64->string. (Experimental)\n" \
           "\tCopyright()\n" \
           "\t\tDisplays copyright info.\n" \
           "\tHelp()\n" \
           "\t\tDisplays this text.\n"
    print(help)
def Copyright():
    print(copyright)


if __name__ == '__main__':
    import time
    t = time.time()
    key = CreateKey("SpamSpam")
    #Msg = Encrypt("The quick brown fox jumps over the lazy dog.", key)
    Msg = Encrypt(Translate(open("audio.webm", "rb").read()), key)
    #print(Decrypt(Msg, key))
    open("audio_decr.webm", "wb").write(Translate(Decrypt(Msg, key), "out"))
    #key2 = CreateKey("SpamSpam ")
    #print(Decrypt(Msg, key2))
    print("Duration: " + str(time.time() - t))