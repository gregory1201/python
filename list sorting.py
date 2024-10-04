def count_vowels(s):
    vowels = "aeiou"
    return sum(1 for char in s.lower() if char in vowels)

sentence = input("Enter a sentence: ")
print(f"Number of vowels: {count_vowels(sentence)}")
