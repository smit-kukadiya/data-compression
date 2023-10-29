# Write a program to Implement LZ77 algorithm.

def compress_lz77(input_string, window_size, buffer_size):
    compressed_data = []
    i = 0

    while i < len(input_string):
        match = find_longest_match(input_string, i, window_size, buffer_size)
        if match:
            offset, length = match
            compressed_data.append((offset, length, input_string[i + length]))
            i += length + 1
        else:
            compressed_data.append((0, 0, input_string[i]))
            i += 1

    return compressed_data

def find_longest_match(input_string, current_position, window_size, buffer_size):
    max_length = 0
    offset = 0

    for i in range(1, min(current_position, window_size) + 1):
        for j in range(1, min(len(input_string) - current_position, buffer_size) + 1):
            if input_string[current_position:current_position + j] == input_string[current_position - i:current_position - i + j]:
                if j > max_length:
                    max_length = j
                    offset = i

    if max_length == 0:
        return None
    else:
        return (offset, max_length)

def decompress_lz77(compressed_data):
    decompressed_string = ""
    
    for item in compressed_data:
        offset, length, next_char = item
        if offset == 0:
            decompressed_string += next_char
        else:
            start = len(decompressed_string) - offset
            for i in range(length):
                decompressed_string += decompressed_string[start + i]
            decompressed_string += next_char
    
    return decompressed_string


if __name__ == '__main__':
    input_string = input("Enter input string: ")
    window_size = int(input("Enter window size: "))
    buffer_size = int(input("Enter buffer size: "))

    compressed_data = compress_lz77(input_string, window_size, buffer_size)
    print("Compressed Data:", compressed_data)

    decompressed_string = decompress_lz77(compressed_data)
    print("Decompressed String:", decompressed_string)
