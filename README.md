# PCA
<b>Portable crypting algorithm</b> - short and easy cryptographic library for python 3.5+ (for now).

## How to use?
So, short code for start:

    import PCA  
    import time
    t = time.time()
    key = CreateKey("SpamSpam")
    Msg = Encrypt("The quick brown fox jumps over the lazy dog.", key)
    print(Decrypt(Msg, key))
    print("Duration: " + str(time.time() - t))

Here you can see, how simple it is.
If you still don't undestand it, try to call <code>PCA.Help()</code>.

### Requirements
You need following modules (included in python 3):
* hashlib
* json
* base64
* random

#### Vulnerabilities
For now - if you find some, contact me and i will try to solve them as soon as possible.

### Detailed guide
Functions availible:
* CreateKey(string) 
    * _returns string_
    * Key have to be larger than eight letters, minimal recommended length is __16__
* Encrypt(string, key) 
    * _returns string_
    * Is recommended to be multiple of 16, in best case multiple of __64__
* Decrypt(string, key)
    * _returns string_
* Translate(bytes, mode)
    * _return base64 string_
    * use to translate (for example) image data or other files such as .exe, .doc, .. to string, which can be encrypted.
    * Modes __"in"__ and __"out"__, IN: file->base64, OUT: base64->file
* Help()
    * _print help message_
* Copyright()
    * _print copyright info_
