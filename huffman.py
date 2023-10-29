# Write a program to generate Huffman code.

import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(characters, frequencies):
    nodes = [Node(char, freq) for char, freq in zip(characters, frequencies)]
    heapq.heapify(nodes)

    while len(nodes) > 1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)
        parent = Node(None, left.freq + right.freq)
        parent.left = left
        parent.right = right
        heapq.heappush(nodes, parent)

    return nodes[0]

def generate_huffman_codes(root, code, huffman_codes):
    if root is None:
        return

    if root.char is not None:
        huffman_codes[root.char] = code
        return

    generate_huffman_codes(root.left, code + "0", huffman_codes)
    generate_huffman_codes(root.right, code + "1", huffman_codes)

def huffman_codes(characters, frequencies):
    root = build_huffman_tree(characters, frequencies)
    huffman_codes = {}
    generate_huffman_codes(root, "", huffman_codes)
    return huffman_codes

characters = input("Enter characters: ").split()
frequencies = [ float(frequency) for frequency in input("Enter frequencies: ").split() ]

huffman_codes_dict = huffman_codes(characters, frequencies)
for char, code in huffman_codes_dict.items():
    print(f"Character: {char}, Huffman Code: {code}")
