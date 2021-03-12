def reverse_string(word):
    size = len(word)
    result = ""
    for i in range(size - 1, -1, -1):
        result += word[i]
    return result

word = input()
reversed_word = reverse_string(word)
if(word == reversed_word):
    print("Palindrome")
else:
    print("Not a palindrome")