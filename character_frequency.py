def display_character_frequencies(input_string):
    if not isinstance(input_string, str):
        print("Please provide a valid string.")
        return
    
    num_numeric = sum(c.isdigit() for c in input_string)
    num_lowercase = sum(c.islower() for c in input_string)
    num_uppercase = sum(c.isupper() for c in input_string)
    num_symbols = len(input_string) - num_numeric - num_lowercase - num_uppercase
    
    print(f"Character Frequencies:\n- Numeric: {num_numeric}\n- Lowercase: {num_lowercase}\n- Uppercase: {num_uppercase}\n- Symbols: {num_symbols}")

    
test_strings = [
    "n<V}wePdAA`9kE2?",
    "u@jmzB=\"nMLLH6Ee",
    "K}s?3UdG_t:m=+Wz",
    "N7pKt`N/Y2Pcr/mS",
    "K^5Vk&EA!?`6aB@$",
]

for test_string in test_strings:
    display_character_frequencies(test_string)
    print("---")