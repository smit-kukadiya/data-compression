# Write a program to generate binary code for the sequence abacabb, Given the frequency count of a – 37, b-38, c-25.

import heapq
from collections import defaultdict

class Node:
    def __init__(self, character, frequency):
        self.character = character
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency

def generate_huffman_tree(frequencies):
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.frequency + right.frequency)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    
    return heap[0]

def generate_huffman_codes(root):
    codes = {}
    
    def traverse(node, code):
        if node.character is not None:
            codes[node.character] = code
            return
        if node.left:
            traverse(node.left, code + '0')
        if node.right:
            traverse(node.right, code + '1')
    
    traverse(root, '')
    return codes

frequencies = {'a': 37, 'b': 38, 'c': 25}

huffman_tree = generate_huffman_tree(frequencies)

huffman_codes = generate_huffman_codes(huffman_tree)

for char, code in huffman_codes.items():
    print(f"Character '{char}': {code}")

sequence = "abacabb"
encoded_sequence = ''.join(huffman_codes[char] for char in sequence)
print(f"Encoded Sequence: {encoded_sequence}")