# Given the code as sequence of characters and given the probability of characters, write a program to calculate average length of each code.

def calculate_average_code_length(characters, probabilities):
    if len(characters) != len(probabilities):
        raise ValueError("The number of characters and probabilities must be the same.")
    
    average_length = 0.0

    for i in range(len(characters)):
        character = characters[i]
        probability = probabilities[i]
        code_length = len(character)
        average_length += probability * code_length

    return average_length

characters = input("Enter characters: ").split(" ")
probabilities = [ float(probability) for probability in input("Enter probabilities: ").split(" ") ]

average_length = calculate_average_code_length(characters, probabilities)
print(f"Average code length: {average_length}")