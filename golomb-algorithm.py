# Write a program to Implement Golomb code algorithm.

def golomb_encode(value, m):
    quotient = value // (2**m)
    unary_code = "1" * quotient + "0"
    binary_code = format(value % (2**m), f"0{m}b")
    return unary_code + binary_code

def golomb_decode(encoded_string, m):
    i = 0
    while i < len(encoded_string) and encoded_string[i] == "1":
        i += 1
    quotient = i
    i += 1
    binary_code = encoded_string[i:i+m]
    remainder = int(binary_code, 2)
    return quotient * (2**m) + remainder

if __name__ == '__main__':
    value = int(input("Enter value: "))
    m = int(input("Enter golomb parameter m: "))

    encoded_value = golomb_encode(value, m)
    print(f"Encoded Value (m={m}): {encoded_value}")

    decoded_value = golomb_decode(encoded_value, m)
    print(f"Decoded Value: {decoded_value}")
