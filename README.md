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

