# Write a program to implement Arithmetic algorithm.

class ArithmeticEncoder:
    def __init__(self, text):
        self.text = text
        self.low = 0.0
        self.high = 1.0
        self.range = 1.0

    def encode(self, probabilities):
        for symbol in self.text:
            low_range = self.low
            high_range = self.low + self.range * probabilities[symbol]
            self.low = low_range
            self.range = high_range - low_range

    def get_encoded_value(self):
        return (self.low + self.range) / 2

class ArithmeticDecoder:
    def __init__(self, encoded_value, length):
        self.encoded_value = encoded_value
        self.low = 0.0
        self.high = 1.0
        self.range = 1.0
        self.length = length

    def decode(self, probabilities):
        decoded_text = []
        for _ in range(self.length):
            range_size = self.high - self.low
            cumulative = 0.0
            symbol = None

            for sym, prob in probabilities.items():
                high_limit = self.low + range_size * cumulative + range_size * prob
                if self.low < self.encoded_value <= high_limit:
                    symbol = sym
                    self.high = high_limit
                    break
                cumulative += prob

            if symbol is None:
                break

            decoded_text.append(symbol)
            self.encoded_value = (self.encoded_value - self.low) / range_size
            self.low = self.low + range_size * cumulative
            self.range = range_size * prob

        return ''.join(decoded_text)

if __name__ == '__main__':
    characters = input("Enter characters: ").split(" ")
    probabilities = [ float(probability) for probability in input("Enter probabilities: ").split(" ") ]
    characters_probabilities = dict(zip(characters, probabilities))
    message = input("Enter message: ")
    
    encoder = ArithmeticEncoder(message)
    encoder.encode(characters_probabilities)
    encoded_value = encoder.get_encoded_value()

    decoder = ArithmeticDecoder(encoded_value, len(message))
    decoded_text = decoder.decode(characters_probabilities)

    print("Encoded Value:", encoded_value)
    print("Decoded Text:", decoded_text)