def is_palindrome(word):
    word = word.lower()

    stack = []

    for char in word:
        stack.append(char)

    reversed_word = ""
    while stack:
        reversed_word += stack.pop()

    return word == reversed_word

word = input("Enter a word to check if it's a palindrome: ")
if is_palindrome(word):
    print(f'"{word}" is a palindrome.')
else:
    print(f'"{word}" is not a palindrome.')