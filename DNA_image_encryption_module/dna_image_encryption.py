# Link to paper: https://d1wqtxts1xzle7.cloudfront.net/55105101/pxc3893440-libre.pdf?1511585057=&response-content-disposition=inline%3B+filename%3DA_New_Image_Encryption_Algorithm_based_o.pdf&Expires=1701984812&Signature=I5M-0ANyJUWOtok7meTc2ryLKyHtWlEb0Fsv~lby7u4Hq84W2hRRSos0uTLe9~fHbKmUhXLfUyXWC-l24c9lcWat-X7reQvP9~86re70z6dCxA-xHO0oOkvFhGYywpBV7Nl30z~5XnpAtAtWq2MBodjLCZrW30yGSAjrhojn2URFDy30enszXJ5-S1k3rHYjutPP-yYCsk6XpVnhmXS7C8qn35vxH3lYJ2KsFOE78U-VveCz87VVyx5GBPcU1WBpitKBqdkuPEfX6Y-XgzTczjfjGZ2KNqQGILARSJKs2HME~UforiNrI8HQTxAZZ4~MP31wnFV1l3aIja79HBsMxw__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA

from PIL import Image
from numpy import asarray
import numpy as np

import useful_stuff

def encrypt_image(image_name):
    IV, key_sequence = useful_stuff.get_IV_and_key_sequence()

    image = Image.open(image_name)
    data = asarray(image)
    shape = data.shape

    P = useful_stuff.convert_3d_to_1d(data)
    P_binary = useful_stuff.convert_decimal_to_binary_str(P)

    C = []
    C_dna = []
    X = []
    X_decimal = []
    for i in range(len(P_binary)):
        if i==0:
            C.append(useful_stuff.binary_addition(useful_stuff.binary_xor(P_binary[i],IV),key_sequence[i]))
            C_dna.append(useful_stuff.convery_binary_to_dna(C[i]))
            # X.append(useful_stuff.dna_computation_by_pixel(C_dna[i],useful_stuff.complement_dna(useful_stuff.rotate_dna(C_dna[len(C_dna)-1],2)),'+'))
            # Tanmayi: Change in logic
            X.append(C_dna[i])
            X_decimal.append(useful_stuff.binary_to_decimal(useful_stuff.convert_dna_to_binary(X[i])))
            continue
        # Tanmayi: Change in logic
        # C.append(useful_stuff.binary_addition(useful_stuff.binary_xor(P_binary[i],C[i-1]),key_sequence[i%len(key_sequence)]))
        C.append(useful_stuff.binary_addition(useful_stuff.binary_xor(P_binary[i], P_binary[i - 1]),key_sequence[i % len(key_sequence)]))
        C_dna.append(useful_stuff.convery_binary_to_dna(C[i]))
        X.append(useful_stuff.dna_computation_by_pixel(C_dna[i],useful_stuff.complement_dna(useful_stuff.rotate_dna(X[i - 1], 2)),'+'))
        X_decimal.append(useful_stuff.binary_to_decimal(useful_stuff.convert_dna_to_binary(X[i])))


    reconstructed_data = asarray(useful_stuff.convert_1d_to_3d(X_decimal,shape))
    reconstructed_data = reconstructed_data.astype(np.uint8)

    image = Image.fromarray(asarray(reconstructed_data))
    # image.show()
    image.save("/Users/tanmayi.nandan/PycharmProjects/DNA_image_encryption/images/interview-group-pic_encrypted_image.png")


encrypt_image('/Users/tanmayi.nandan/PycharmProjects/DNA_image_encryption/images/interview-group-pic.png')