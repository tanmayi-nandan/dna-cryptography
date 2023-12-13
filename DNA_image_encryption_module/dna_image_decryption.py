# Link to paper: https://d1wqtxts1xzle7.cloudfront.net/55105101/pxc3893440-libre.pdf?1511585057=&response-content-disposition=inline%3B+filename%3DA_New_Image_Encryption_Algorithm_based_o.pdf&Expires=1701984812&Signature=I5M-0ANyJUWOtok7meTc2ryLKyHtWlEb0Fsv~lby7u4Hq84W2hRRSos0uTLe9~fHbKmUhXLfUyXWC-l24c9lcWat-X7reQvP9~86re70z6dCxA-xHO0oOkvFhGYywpBV7Nl30z~5XnpAtAtWq2MBodjLCZrW30yGSAjrhojn2URFDy30enszXJ5-S1k3rHYjutPP-yYCsk6XpVnhmXS7C8qn35vxH3lYJ2KsFOE78U-VveCz87VVyx5GBPcU1WBpitKBqdkuPEfX6Y-XgzTczjfjGZ2KNqQGILARSJKs2HME~UforiNrI8HQTxAZZ4~MP31wnFV1l3aIja79HBsMxw__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA

from PIL import Image
from numpy import asarray
import numpy as np

import useful_stuff


def decrypt_image(image_name):
    IV, key_sequence = useful_stuff.get_IV_and_key_sequence()

    image = Image.open(image_name)
    data = asarray(image)
    shape = data.shape

    X_decimal = useful_stuff.convert_3d_to_1d(data)
    X_binary = useful_stuff.convert_decimal_to_binary_str(X_decimal)
    X = useful_stuff.convert_binary_to_dna_str(X_binary)

    C = []
    C_dash = []
    P_dash = []
    final_P = []
    for i in range(len(X)):
        if i==0:
            # C.append(useful_stuff.dna_computation_by_pixel(X[i], useful_stuff.complement_dna(useful_stuff.rotate_dna_right(X[len(X) - 1], 2)), '-'))
            # Tanmayi: Change in logic
            C.append(X[0])
            C_dash.append(useful_stuff.convert_dna_to_binary(C[i]))
            P_dash.append(useful_stuff.binary_xor(useful_stuff.binary_subtraction(C_dash[i], key_sequence[i]), IV))
            final_P.append(useful_stuff.binary_to_decimal(P_dash[i]))
            continue
        C.append(useful_stuff.dna_computation_by_pixel(X[i], useful_stuff.complement_dna(useful_stuff.rotate_dna_right(X[i-1], 2)), '-'))
        C_dash.append(useful_stuff.convert_dna_to_binary(C[i]))
        P_dash.append(useful_stuff.binary_xor(useful_stuff.binary_subtraction(C_dash[i], key_sequence[i % len(key_sequence)]),P_dash[i - 1]))
        final_P.append(useful_stuff.binary_to_decimal(P_dash[i]))


    reconstructed_P = asarray(useful_stuff.convert_1d_to_3d(final_P,shape))
    reconstructed_P = reconstructed_P.astype(np.uint8)

    image = Image.fromarray(reconstructed_P)
    image.show()
    image.save("/Users/tanmayi.nandan/PycharmProjects/DNA_image_encryption/images/interview-group-pic_decrypted_image.png")


decrypt_image('/Users/tanmayi.nandan/PycharmProjects/DNA_image_encryption/images/interview-group-pic_encrypted_image.png')