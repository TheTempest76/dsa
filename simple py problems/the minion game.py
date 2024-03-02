def minion_game(s):
    # your code goes here
    vowels = ['A', 'E', 'I', 'O', 'U']

    a = 0
    b = 0
    for i, c in enumerate(s):
        if c in vowels:
            b += len(s) - i
        else:
            a += len(s) - i

    if a == b:
        print ("Draw")
    elif a > b:
        print(f"Stuart {b}")
    else:
        print(f"Stuart {a}")
    
print(minion_game("banana"))