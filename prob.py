text = input()
n = len(text)
for i in range(0, n):
    c = text[i]
    if(c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'):
        print("#", end = '')
    else
        print("$", end = '')