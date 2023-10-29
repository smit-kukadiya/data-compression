# Given the sequence of characters, write a program to find unique characters, and write a program to implement ppma algorithm.

import random

class PPMA:
    def __init__(self, order):
        self.order = order
        self.contexts = {}
        self.total_counts = {}

    def train(self, text):
        for i in range(len(text)):
            context = text[max(0, i - self.order):i]
            current_char = text[i]
            if context not in self.contexts:
                self.contexts[context] = {}
            if current_char not in self.contexts[context]:
                self.contexts[context][current_char] = 1
            else:
                self.contexts[context][current_char] += 1
            if context not in self.total_counts:
                self.total_counts[context] = 1
            else:
                self.total_counts[context] += 1

    def encode(self, text):
        encoded_data = []
        i = 0
        while i < len(text):
            j = i + 1
            context = text[i:j]
            while context in self.contexts and j <= len(text):
                j += 1
                context = text[i:j]
            j -= 1
            context = text[i:j]
            encoded_data.append(context)
            i = j
        return encoded_data

    def decode(self, encoded_data):
        decoded_text = ""
        for context in encoded_data:
            if context in self.contexts:
                probabilities = self.contexts[context]
                total_count = self.total_counts[context]
                char = self.select_char(probabilities, total_count)
                decoded_text += char
                self.update_model(context, char)
        return decoded_text

    def select_char(self, probabilities, total_count):
        r = random.random()
        cumulative_prob = 0
        for char, count in probabilities.items():
            cumulative_prob += count / total_count
            if r < cumulative_prob:
                return char
        return list(probabilities.keys())[-1]

    def update_model(self, context, char):
        if context in self.contexts:
            if char in self.contexts[context]:
                self.contexts[context][char] += 1
            else:
                self.contexts[context][char] = 1
            self.total_counts[context] += 1


if __name__ == '__main__':
    input_text = input("Enter input text: ")

    order = 1
    ppma = PPMA(order)
    ppma.train(input_text)
    
    encoded_data = ppma.encode(input_text)
    print("Encoded Data:", encoded_data)
    
    decoded_text = ppma.decode(encoded_data)
    print("Decoded Text:", decoded_text)
