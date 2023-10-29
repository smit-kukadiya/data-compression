# Python program for the above approach

def search(input_char, lst):
	for i in range(len(lst)):
		if lst[i] == input_char:
			return i

def move_to_front(curr_index, lst):
	record = lst[:]
	lst[1:curr_index+1] = record[:curr_index]
	lst[0] = record[curr_index]

def mtf_encode(input_text, lst):
	output_arr = []
	text = []

	for i in range(len(input_text)):
		output_arr.append(search(input_text[i], lst))
        
		print(output_arr[i], end=' ')
		text.append(output_arr[i])

		move_to_front(output_arr[i], lst)
	return text
		
def mtf_decode(arr):
    lst = list("abcdefghijklmnopqrstuvwxyz")
    result = []
    for i in arr:
        result.append(lst[i])
        move_to_front(i, lst)
    return ''.join(result)

def main():
	input_text = input("Enter text: ")
	len_text = len(input_text)

	lst = list("abcdefghijklmnopqrstuvwxyz")

	print(f"Input text: {input_text}")
	print(f"Move to Front Transform: ", end='')

	text = mtf_encode(input_text, lst)
	print(f"\nDecoded text: {mtf_decode(text)}")

if __name__ == "__main__":
	main()
