i = 0
# terminate if we meet 5
lst = ["apple", "pear", "kiwi", "peach"]
while i < len(lst) - 1:
    print(lst[i])
    i += 1
    if len(lst[i]) <= 4:
        continue
    
    
