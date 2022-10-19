# SHA256-WordHash
**Python program that uses hashlib library to find words whose ASCII encoding corresponds to a given SHA-256 digest.**



**q1.py**
________________
q1.py uses hashlib library to find words whose ASCII encoding corresponds to a given SHA-256 digest.









**q3.py** 
________________
**q3.py contains two functions encrypt and decrypt.** 

**encrypt(message, key) implements the following symmetric encryption algorithm which accepts a shared 8-bit key:**

  - Breaks the plaintext into a list of characters.
  
  
  - Places the ASCII code of every four consecutive characters of the plaintext into a single word (4-bytes) packet.
  
  
  - Encrypt each packet by finding the bit-wise exclusive-or of the packet and the given key after extending the key. For example, if the key is 0x4b, the extended key is 0x4b4b4b4b.
  
      - each packet gets encrypted separately, but the results of encrypting packets are concatenated together to generate the ciphertext.
    
 **decrypt(cipher, key) gets the ciphertext and the key as input and returns the plaintext as output.**
  
  
  
