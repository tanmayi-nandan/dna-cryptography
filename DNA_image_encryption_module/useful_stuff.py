import numpy as np

dna_combinations = [
    {'00':'A', '01':'C', '10':'G', '11':'T'}, # Rule 1
    {'00':'A', '01':'G', '10':'C', '11':'T'}, # Rule 2
    {'00':'C', '01':'A', '10':'T', '11':'G'}, # Rule 3
    {'00':'C', '01':'T', '10':'A', '11':'G'}, # Rule 4
    {'00':'G', '01':'A', '10':'T', '11':'C'}, # Rule 5
    {'00':'G', '01':'T', '10':'A', '11':'C'}, # Rule 6
    {'00':'T', '01':'C', '10':'G', '11':'A'}, # Rule 7
    {'00':'T', '01':'G', '10':'C', '11':'A'}  # Rule 8
]

def get_IV_and_key_sequence():
    # initialization vector
    IV = '10101010'

    # generate key
    # key = [97, 11, 178, 34, 2, 87, 111, 213, 19, 220, 178, 120, 50, 79, 145, 5, 111]  actual
    key = [97, 11, 178, 34, 2, 87, 111, 213, 19, 220, 178, 120, 50, 79, 145, 5, 110]   # trial
    key_sequence = []
    for i in key:
        key_sequence.append(convert_to_binary_8dig(str(i)))
    return (IV,key_sequence)

def convert_to_binary_8dig(n):
    zeroes = 0
    for i in range(0,len(n)):
        if n[i]=='0':
            zeroes+=1
            continue
        break
    n = int(n)
    # print(f'Zeroes: {zeroes}')
    binary = bin(n).replace("0b", "")
    diff = 8 - len(binary)
    if diff>0:
        for i in range(0,diff):
            binary = '0'+binary
    # print(binary)
    return binary

def convery_binary_to_dna(binary):
    diff = 8 - len(binary)
    if diff > 0:
        for i in range(0, diff):
            binary = '0' + binary
    dna_encoded = ''
    for i in range(0,len(binary),2):
        binary_bit = binary[i]+binary[i+1]
        # print(binary_bit)
        # Using the Rule-1 from DNA combinations by default
        dna_encoded = dna_encoded + dna_combinations[0][binary_bit]
    # print(dna_encoded)
    return (dna_encoded)

def convert_dna_to_binary(dna):
    dna_binary = ''
    dna_conversion = dna_combinations[0]
    for letter in list(dna):
        dna_binary += list(dna_conversion.keys())[list(dna_conversion.values()).index(letter)]
    return dna_binary

def convert_binary_to_dna(binary):
    dna = ''
    dna_conversion = dna_combinations[0]
    for i in range(0,len(binary),2):
        dna += dna_conversion[binary[i:i+2]]
    return dna

def convert_decimal_to_binary(decimal_number):
    binary_representation = bin(decimal_number)[2:]
    return binary_representation

def xor(A,B):
    if A=='0' and B=='0':
        return '0'
    if A=='0' and B=='1':
        return '1'
    if A=='1' and B=='0':
        return '1'
    if A=='1' and B=='1':
        return '0'

def binary_xor(bin_str1, bin_str2):
    # Ensure that the binary strings have the same length
    if len(bin_str1) != len(bin_str2):
        # raise ValueError("Binary strings must have the same length for XOR operation.")
        diff = 8 - len(bin_str1)
        if diff>0:
            for i in range(0,diff):
                bin_str1 = '0'+bin_str1
        diff = 8 - len(bin_str2)
        if diff>0:
            for i in range(0,diff):
                bin_str2 = '0'+bin_str2

    # Perform XOR on corresponding bits
    result = ''.join('1' if a != b else '0' for a, b in zip(bin_str1, bin_str2))

    return str(result)

def binary_addition(bin_str1, bin_str2):
    # Convert binary strings to integers
    num1 = int(str(bin_str1), 2)
    num2 = int(str(bin_str2), 2)

    # Perform binary addition
    result = num1 + num2
    result = result % 256

    # Convert the result back to binary
    result_bin = bin(result)[2:]

    # Make sure its 8 bits
    diff = 8 - len(result_bin)
    if diff > 0:
        for i in range(0, diff):
            result_bin = '0' + result_bin

    return result_bin

def binary_subtraction(bin_str1, bin_str2):
    # Convert binary strings to integers
    num1 = int(bin_str1, 2)
    num2 = int(bin_str2, 2)

    # Perform binary subtraction
    result = num1 - num2

    # Apply modulo 256 if the result is negative
    result = result % 256 if result < 0 else result

    # Convert the result back to binary
    result_bin = bin(result)[2:]

    # Make sure its 8 bits
    diff = 8 - len(result_bin)
    if diff > 0:
        for i in range(0, diff):
            result_bin = '0' + result_bin

    return result_bin

def rotate_dna(dna_str,i):
    i = i % 4
    rotated_str = dna_str[i:] + dna_str[:i]
    return rotated_str

def rotate_dna_right(dna_str, i):
    i = i % 4
    rotated_str = dna_str[-i:] + dna_str[:-i]
    return rotated_str

def complement_dna(dna_str):
    # print(dna_str)
    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    complemented_str = ''.join(complement_dict[base] for base in dna_str)
    return complemented_str

def dna_computation(X,Y,op):
    addition={
        'C': {'C': 'C', 'T': 'T', 'A': 'A', 'G': 'G'},
        'T': {'C': 'T', 'T': 'A', 'A': 'G', 'G': 'C'},
        'A': {'C': 'A', 'T': 'G', 'A': 'C', 'G': 'T'},
        'G': {'C': 'G', 'T': 'C', 'A': 'T', 'G': 'A'},
    }
    subtraction = {
        'C': {'C': 'C', 'T': 'G', 'A': 'A', 'G': 'T'},
        'T': {'C': 'T', 'T': 'C', 'A': 'G', 'G': 'A'},
        'A': {'C': 'A', 'T': 'T', 'A': 'C', 'G': 'G'},
        'G': {'C': 'G', 'T': 'A', 'A': 'T', 'G': 'C'},
    }
    if op=='+':
        return addition[X][Y]
    if op=='-':
        return subtraction[X][Y]

def dna_computation_by_pixel(strX, strY, op):
    if len(strX)!=len(strY):
        return None
    ans = ''
    for i in range(0,len(strX)):
        ans += dna_computation(strX[i],strY[i],op)
    return ans

def binary_to_decimal(binary_str):
    decimal_value = int(binary_str, 2)
    return decimal_value

def convert_3d_to_1d(data):
    P = []
    for i in range(0, len(data)):
        # print(data[i])
        for j in range(0, len(data[i])):
            # print(len(data[i][j]))
            for k in range(0, len(data[i][j])-1):
                P.append(data[i][j][k])
    return P

def convert_3d_to_1d_direct(data_3d):
    # Flatten the 3D array
    flattened_data = np.ravel(data_3d)

    return flattened_data

def convert_decimal_to_binary_str(P):
    # convert P into binary
    P_binary = []
    for i in P:
        P_binary.append(convert_to_binary_8dig(str(i)))
    return P_binary

def convert_binary_to_dna_str(C):
    C_dna = []
    for i in C:
        C_dna.append(convert_binary_to_dna(i))
    return C_dna

def convert_1d_to_3d(X_decimal,shape):
    # X_decimal = X_decimal.astype(np.uint8)
    reconstructed_data = []
    index = 0
    for i in range(shape[0]):
        row_data = []
        for j in range(shape[1]):
            element_data = X_decimal[index:index + shape[2]-1]
            element_data.append(255)
            # print(element_data)
            row_data.append(element_data)
            index += (shape[2]-1)
        reconstructed_data.append(row_data)
        # break
    # reconstructed_data = asarray(reconstructed_data)
    return reconstructed_data

def convert_1d_to_3d_direct(flattened_data, shape):
    # Calculate the expected shape based on the total number of elements
    expected_shape = shape if np.prod(shape) == flattened_data.size else None

    if expected_shape is not None:
        # Reshape the flattened data to the original 3D shape
        data_3d = flattened_data.reshape(expected_shape)
        return data_3d
    else:
        raise ValueError("Incompatible shape and flattened data size.")
