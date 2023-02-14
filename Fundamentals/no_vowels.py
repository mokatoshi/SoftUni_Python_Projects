input_text = input()

new_word = [vowels for vowels in input_text if vowels.lower() not in ["a", "o", "u", "e", "i" ]]

print("".join(new_word))

