# Write a program to Implement LZ78 algorithm.

def compress_lz78(input_string):
    dictionary = [""]
    compressed_data = []
    current_match = ""

    for char in input_string:
        current_match += char
        if current_match not in dictionary:
            dictionary.append(current_match)
            compressed_data.append((dictionary.index(current_match[:-1]), current_match[-1]))
            current_match = ""

    if current_match:
        compressed_data.append((dictionary.index(current_match), ''))

    return compressed_data

def decompress_lz78(compressed_data):
    dictionary = [""]
    decompressed_string = ""

    for index, char in compressed_data:
        entry = dictionary[index] + char
        dictionary.append(entry)
        decompressed_string += entry

    return decompressed_string

if __name__ == '__main__':
    input_string = input("Enter input string: ")

    compressed_data = compress_lz78(input_string)
    print("Compressed Data:", compressed_data)

    decompressed_string = decompress_lz78(compressed_data)
    print("Decompressed String:", decompressed_string)
