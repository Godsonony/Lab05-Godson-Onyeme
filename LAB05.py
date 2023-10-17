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

def count_vowels_rec(sentence):
    # Base case: if the sentence is empty, return 0
    if len(sentence) == 0:
        return 0

    # Check if the first character of the sentence is a vowel
    if is_vowel(sentence[0]):
        # If it's a vowel, add 1 and recursively count the vowels in the rest of the sentence
        return 1 + count_vowels_rec(sentence[1:])
    else:
        # If it's not a vowel, just recursively count the vowels in the rest of the sentence
        return count_vowels_rec(sentence[1:])

# Example calls to the function
print(count_vowels_rec('this is a sentence'))  # returns 6
print(count_vowels_rec('loud'))               # returns 2
print(count_vowels_rec('rebel'))              # returns 2

def my_reduce(values, start_val, op):
    current_value = start_val

    for value in values:
        current_value = op(current_value, value)

    return current_value

# Example call to the function
values = [1, 2, 3, 4, 5]
sum_of_values = my_reduce(values, 0, lambda x, y: x + y)
print(sum_of_values)  # Output should be 15
