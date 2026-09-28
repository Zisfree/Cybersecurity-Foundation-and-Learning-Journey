# What is cryptogrpaahy?
- Cryptography is hiding the actual text in non readable texts. It is used to hide or secure important information.

### ASCII
- ASCII charecters are 7 bit encoded charecters in form of integers from 0-127
- Like if we have a list of integers *72,97,118,101,32,115,111,109,101,32,115,104,97,109,101*, we can use this an input in any int to ASCII converter site and solve it.
- Or maybe just use a python program.[https://github.com/Zisfree/Cybersecurity-Foundation-and-Learning-Journey/blob/main/python/Crypto%20pythons/crypto_1.py]

### Hex
- Hex, short for hexadecimal are 16 bit encoded character. Hex uses bas16 to encode.
- We can input our hex and use a character encoder to convert it into normal text. In this case we use ASCII as our character encoder. [https://github.com/Zisfree/Cybersecurity-foundations-and-tool-integration-lab/blob/main/Deep-Dives/What%20does%20a%20charecter%20encoder%20do.md]
- Like I have this *736D6172746E6573732066726F6D206E6F7468696E67* hex code.
- For the python way [https://github.com/Zisfree/Cybersecurity-Foundation-and-Learning-Journey/blob/main/python/Crypto%20pythons/crypto_2.py]

### Base64
- Base64 is a 6 bit encoded character.
- It is the most used on websites. Convert your image or videos else into base64 and put it inside the code. It reads is without needing to download any file.
- It reads the files in in 6 bits where a standard byte is 8 bit. To overcome this it just divides the whole lowest common multiple of both 6 and 8.[]
- For python - [https://github.com/Zisfree/Cybersecurity-Foundation-and-Learning-Journey/blob/main/python/Crypto%20pythons/crypto_3.py]

### Base10
- The advanced encryption, like RSA don't understand what an alphabet is. They only understand mathematics.
- So we convert our data into hex/base16 then into a base10.
- Like if we have *1937076257*. This is a base10 [https://github.com/Zisfree/Cybersecurity-Foundation-and-Learning-Journey/blob/main/python/Crypto%20pythons/crypto_4.py]

### ⊕ XOR
- XOR is a bitwise operator (which use 0's and 1's). It prints 0 if bits are same and 1 if they are different.
- It is denoted or used by ⊕/^. [https://github.com/Zisfree/Cybersecurity-foundations-and-tool-integration-lab/blob/main/Deep-Dives/XOR.md]
- Using python [https://github.com/Zisfree/Cybersecurity-Foundation-and-Learning-Journey/blob/main/python/Crypto%20pythons/crypto_5.py]
