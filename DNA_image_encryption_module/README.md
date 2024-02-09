# Implementation of A New Image Encryption Algorithm based on DNA Approach

R. Gupta et al. propose a novel image encryption algorithm based on DNA which uses a Cipher Block Chaining (CBC) mode of encryption. The proposed algorithm also involves binary as well as DNA computations during encryption in CBC mode, which provides added security to the cryptosystem, and hence was selected for implementation. 



## DNA Image Encryption Module

The process begins with flattening the pixel array obtained from an image into 1D, which is then converted into binary values, providing a format suitable for subsequent encryption steps. An initialization vector (IV) is used for the first computation, followed by a CBC mode of using the previous encrypted value. The computation involves an XOR operation between the key sequence, the plaintext and the previous encrypted value. The sequence is then encoded into DNA, rotated, complemented, and DNA addition is performed. The DNA sequence is then converted back to binary and decimal form, from which the encrypted image is constructed.

![Flowchart](images/flowchart.png)


## DNA Image Decryption Module

The decryption process was not stated in the paper but was built while following the same sequence of steps in reverse order. 

Note: The generation of the IV and key sequence fell outside our scope and were thus assumed.
