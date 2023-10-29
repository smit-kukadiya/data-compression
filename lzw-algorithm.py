# Write a program to Implement LZW algorithm.

def compress_lzw(input_string):
    dictionary = {chr(i): i for i in range(256)}
    next_code = 257
    result = []
    current_match = ""

    for char in input_string:
        current_match += char
        if current_match not in dictionary:
            result.append(dictionary[current_match[:-1]])
            dictionary[current_match] = next_code
            next_code += 1
            current_match = char

    if current_match:
        result.append(dictionary[current_match])

    return result

def decompress_lzw(compressed_data):
    dictionary = {i: chr(i) for i in range(256)}
    next_code = 257
    result = [chr(compressed_data[0])]
    current_match = chr(compressed_data[0])

    for code in compressed_data[1:]:
        if code not in dictionary:
            entry = current_match + current_match[0]
        else:
            entry = dictionary[code]

        result.append(entry)
        dictionary[next_code] = current_match + entry[0]
        next_code += 1
        current_match = entry

    return ''.join(result)

# Example usage
if __name__ == '__main__':
    input_string = input("Enter input string: ")

    compressed_data = compress_lzw(input_string)
    print("Compressed Data:", compressed_data)

    decompressed_string = decompress_lzw(compressed_data)
    print("Decompressed String:", decompressed_string)
