def is_vowel(character):
    # Convert the character to lowercase to handle both uppercase and lowercase vowels
    character = character.lower()
    
    # Check if the character is one of the vowels
    if character in ['a', 'e', 'i', 'o', 'u']:
        return True
    else:
        return False

# Example calls to the function
print(is_vowel('t'))  # returns False
print(is_vowel('o'))  # returns True
print(is_vowel('u'))  # returns True
def is_vowel(character):
    # Convert the character to lowercase to handle both uppercase and lowercase vowels
    def is_vowel(character):
    character = character.lower()
    return character in ['a', 'e', 'i', 'o', 'u']

def count_vowels_iter(sentence):
    count = 0  # Initialize a count to keep track of the number of vowels

    for char in sentence:
        if is_vowel(char):
            count += 1

    return count

# Example calls to the function
print(count_vowels_iter('this is a sentence'))  # returns 6
print(count_vowels_iter('loud'))               # returns 2
print(count_vowels_iter('rebel'))              # returns 2